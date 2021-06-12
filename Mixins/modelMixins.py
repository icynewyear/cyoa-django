from django.db import models
from django.utils.timezone import now
from django.template.defaultfilters import slugify


class TrackModelMixin(models.Model):
    class Meta:
        abstract=True

    created_date = models.DateTimeField(blank=True,  default=now)
    modified_date = models.DateTimeField(blank=True, auto_now=True)


class SlugModelMixin(models.Model):
    class Meta:
        abstract=True
    #override to change default field that gets sluggified
    slugged_field_name = "name"
    slug_length = 140

    slug = models.SlugField(null=True, max_length=slug_length)

    def save(self, *args, **kwargs):
        self.slug = self.create_slug()
        super().save(*args, **kwargs)

    def create_slug(self):
        to_slug = getattr(self, self.slugged_field_name)
        return slugify(to_slug)

class SortableModelMixin(models.Model):
    class Meta:
        abstract=True

    #override this
    group_by_field = None

    order = models.IntegerField(blank=True, null=True)

    def get_num_sortables(self):
        if self.group_by_field != None:
            group_field = self.group_by_field
            group = getattr(self, self.group_by_field)
            num_sortables = self.__class__.objects.filter(**{group_field: group}).count()
            return num_sortables
        return 0

    def get_next(self, **kwargs):
        if 'position' in kwargs:
            position = kwargs['position']
        else:
            position = self.order

        num = self.get_num_sortables()

        if num != 0 and position < num:
            next = position + 1
            if 'new' in kwargs:
                next = position
            group_field = self.group_by_field
            group = getattr(self, self.group_by_field)
            next_sortable = self.__class__.objects.get(pk=next)
            return next_sortable
        return None

    def get_previous(self, **kwargs):
        if 'position' in kwargs:
            position = kwargs['position']
        else:
            position = self.order
        num = self.get_num_sortables()
        if position > 1:
            next = position - 1
            group_field = self.group_by_field
            group = getattr(self, self.group_by_field)
            next_sortable = self.__class__.objects.get(pk=next)
            return next_sortable
        return None

    def get_forward_sortables(self, **kwargs):
        sortables = []
        num = self.get_num_sortables()
        for x in range(self.order, num):
            if x == self.order and 'new' in kwargs:
                sortables.append(self.get_next(position=x, new=True))
            sortables.append(self.get_next(position=x))
        return sortables

    def cascade_sortables_forward(self):
        sortables = self.get_forward_sortables(new=True)
        for item in reversed(sortables):
            item.order += 1
            item.save()
        return

    def cascade_sortables_backward(self):
        sortables = self.get_forward_sortables(new=True)
        for item in sortables:
            item.order -= 1
            item.save()
        return

    def save(self, *args, **kwargs):
        if not self.pk:
            self.cascade_sortables_forward()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.cascade_sortables_backward()

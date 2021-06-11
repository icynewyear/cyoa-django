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

from django.contrib import admin

from .models import Adventure, Room, Choice
# Register your models here.


admin.site.register(Adventure)
admin.site.register(Room)
admin.site.register(Choice)

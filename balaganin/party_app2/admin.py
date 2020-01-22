from django.contrib import admin
from . import models

class EventListAdmin(admin.ModelAdmin):
    list_display = ("title",  "created", "event_date")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(models.EventList, EventListAdmin)
admin.site.register(models.Category, CategoryAdmin)
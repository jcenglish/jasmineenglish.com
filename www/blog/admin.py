from django.contrib import admin

# Register your models here.
from .models import Tag, Entry


class EntryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    list_display = ('title', 'date_created', 'date_modified', 'date_published')
    list_filter = ['date_published', 'date_created']


admin.site.register(Entry, EntryAdmin)
admin.site.register(Tag)

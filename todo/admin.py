from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title','complete','created')
    list_display_links = [
        'title'
    ]
    list_filter = ['title','complete']
    search_fields = [
        'title',
        'complete'
    ]
admin.site.register(Task, TaskAdmin)

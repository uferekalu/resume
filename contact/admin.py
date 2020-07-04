from django.contrib import admin
from .models import *

# Register your models here.
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('page',)
admin.site.register(FormField, FormFieldAdmin)


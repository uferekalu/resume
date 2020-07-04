from django.contrib import admin
from .models import *

# Register your models here.
class DetailAdmin(admin.ModelAdmin):
    list_display = ('name','phone','email','payment','balance','dept','total','date_created')
admin.site.register(Details, DetailAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('detail','first_name','last_name','phone')
admin.site.register(Profile, ProfileAdmin)

class CoursesRegisteredAdmin(admin.ModelAdmin):
    list_display = ('subjects_registered','date_created')
admin.site.register(CoursesRegistered, CoursesRegisteredAdmin)

class SchoolsAdmin(admin.ModelAdmin):
    list_display = ('sch','date_created')
admin.site.register(Schools, SchoolsAdmin)

class LevelsAdmin(admin.ModelAdmin):
    list_display = ('lev','date_created')
admin.site.register(Levels, LevelsAdmin)

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('fac','date_created')
admin.site.register(Faculty, FacultyAdmin)
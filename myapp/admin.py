from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'roll', 'city',]
    
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display=['id', 'name', ]
    
    
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display=['id', 'title','duration','singer' ]
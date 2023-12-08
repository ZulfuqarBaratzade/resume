from django.contrib import admin
from core.models import *
# Register your models here.


@admin.register(GeneralSetting)
class GeneralSettingsAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','parameter','created_date','updated_date']
    search_fields = ['name','description','parameter']
    list_editable=['name','description']

    class Meta:
        model = GeneralSetting


@admin.register(ImageSetting)
class ImageSettingsAdmin(admin.ModelAdmin):
    list_display = ['id','name','description','file','created_date','updated_date']
    search_fields = ['name','description','file']
    list_editable=['name','description']

    class Meta:
        model = ImageSetting


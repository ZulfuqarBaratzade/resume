from django.contrib import admin
from .models import GeneralSetting,ImageSetting
# Register your models here.

@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','description','parameter',"updated_date","created_date"]
    search_fields=['name','description','parameter']
    list_editable=['description','parameter']

    class Meta:
        model=GeneralSetting

@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','description','image',"updated_date","created_date"]
    search_fields=['name','description','image']
    list_editable=['description','image']

    class Meta:
        model=ImageSetting
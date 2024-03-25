from django.contrib import admin
from .models import GeneralSetting,ImageSetting,TextSetting,Contact
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

@admin.register(TextSetting)
class TextSettingAdmin(admin.ModelAdmin):
    list_display=['id','name','text',"updated_date","created_date"]
    search_fields=['name','text']
    list_editable=['text']

    class Meta:
        model=TextSetting

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display=['id','email','text',"updated_date","created_date"]
    search_fields=['email','text']
    list_editable=['text']
    class Meta:
        model = Contact

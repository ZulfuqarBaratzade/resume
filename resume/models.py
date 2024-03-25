from django.db import models


# Create your models here.
class AbstractModel(models.Model):
    updated_date=models.DateTimeField(
        blank=True,
        auto_now=True,
        verbose_name="updated_data"
    )
    created_date=models.DateField(
        blank=True,
        auto_now_add=True,
        verbose_name="created_data"
    )
    class Meta:
        abstract=True

class GeneralSetting(AbstractModel):
    name=models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="name"
    )
    description=models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="description"
    )
    parameter=models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="parameter"

    )
    
    def __str__(self):
        return f"General settings {self.name}"
    class Meta:
        verbose_name="General Setting"
        verbose_name_plural="General Settings"
        ordering = ("name", "parameter")



class ImageSetting(AbstractModel):
    name=models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="name"
    )
    description=models.CharField(
        default="",
        max_length=254,
        blank=True,
        verbose_name="description"
    )
    image=models.ImageField(
        default='',
        verbose_name='Image',
        help_text="",
        blank=True,
        upload_to='image/',
    )
    def __str__(self):
        return f"Image setting {self.name}"
    class Meta:
        verbose_name="Image Setting"
        verbose_name_plural="Image Settings"
        ordering=("image",)


class TextSetting(AbstractModel):
    name=models.CharField(default='',max_length=254,blank=True,verbose_name='name')
    text=models.TextField(
        default='',
        max_length=1000,
        blank=True,
        verbose_name='text'
    )
    def __str__(self):
        return f"Text {self.name}"

    class Meta:
        verbose_name="Text Setting"
        verbose_name_plural="Text Settings"
        ordering=("text",)

class Contact(AbstractModel):
    email=models.EmailField()
    text=models.TextField(
        default="",
        max_length=1000,
        blank=True,
        verbose_name='text'
    )
    def __str__(self):
        return f"Text {self.text}"
    class Meta:
        verbose_name="Contact"
        verbose_name_plural="Contact Message"
        ordering=("text",)
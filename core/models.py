from django.db import models

# Create your models here.


class GeneralSetting(models.Model):
    name = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name= 'name',


    )
    description=models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name= 'description',
    )
    parameter = models.CharField(
        default='',
        max_length=254,
        blank=True,
        verbose_name= 'parameter',
    )
    updated_date = models.DateTimeField(
        blank=True,
        auto_now=True,
        
    )
    created_date = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )
    def __str__(self):
        return f'General Setting {self.name}'
    class Meta:
        verbose_name = "General Setting"
        verbose_name_plural = "General Setting"
        ordering = ('name',)
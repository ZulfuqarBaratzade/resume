# Generated by Django 4.2.7 on 2023-12-07 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_generalsettings_generalsetting'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalsetting',
            options={'ordering': ('name',), 'verbose_name': 'General Setting', 'verbose_name_plural': 'General Setting'},
        ),
    ]

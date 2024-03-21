# Generated by Django 5.0.3 on 2024-03-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=254, verbose_name='name')),
                ('description', models.CharField(blank=True, default='', max_length=254, verbose_name='description')),
                ('parameter', models.CharField(blank=True, default='', max_length=254, verbose_name='parameter')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_data')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='created_data')),
            ],
            options={
                'verbose_name': 'General Setting',
                'verbose_name_plural': 'General Settings',
                'ordering': ('name', 'parameter'),
            },
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-25 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_textsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='updated_data')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='created_data')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(blank=True, default='', max_length=1000, verbose_name='text')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact Message',
                'ordering': ('text',),
            },
        ),
        migrations.AlterField(
            model_name='textsetting',
            name='text',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='text'),
        ),
    ]

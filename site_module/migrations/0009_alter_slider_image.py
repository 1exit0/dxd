# Generated by Django 4.2.7 on 2023-11-30 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0008_remove_slider_description_alter_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر(972\u200a×\u200a2160)'),
        ),
    ]

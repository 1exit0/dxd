# Generated by Django 4.2.7 on 2023-11-28 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_productgallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='battery_capacity',
            field=models.IntegerField(blank=True, null=True, verbose_name='ظرفیت باتری'),
        ),
        migrations.AddField(
            model_name='product',
            name='display_size',
            field=models.FloatField(blank=True, null=True, verbose_name='سایز صفحه نمایش'),
        ),
        migrations.AddField(
            model_name='product',
            name='internal_memory',
            field=models.IntegerField(blank=True, null=True, verbose_name='حافظه داخلی'),
        ),
        migrations.AddField(
            model_name='product',
            name='processor_type',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='نوع پردازنده'),
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.IntegerField(blank=True, null=True, verbose_name='حافظه RAM'),
        ),
        migrations.AddField(
            model_name='product',
            name='rear_camera',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='دوربین اصلی'),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty',
            field=models.TextField(default=1, max_length=256, verbose_name='گارانتی'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True, verbose_name='عنوان در URL'),
        ),
    ]
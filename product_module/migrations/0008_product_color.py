# Generated by Django 4.2.7 on 2023-11-28 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0007_product_battery_capacity_product_display_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default=1, max_length=20, verbose_name='رنگ محصول'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.7 on 2023-12-04 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0009_productcategory_parent_productcategory_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='priority',
        ),
    ]

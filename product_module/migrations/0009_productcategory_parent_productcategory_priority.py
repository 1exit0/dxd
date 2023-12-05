# Generated by Django 4.2.7 on 2023-12-04 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0008_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='product_module.productcategory', verbose_name='دسته بندی والد'),
        ),
        migrations.AddField(
            model_name='productcategory',
            name='priority',
            field=models.IntegerField(default=1, verbose_name='اولویت نمایش'),
        ),
    ]

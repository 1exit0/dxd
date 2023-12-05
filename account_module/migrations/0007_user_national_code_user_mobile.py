# Generated by Django 4.2.7 on 2023-11-29 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0006_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='National_Code',
            field=models.CharField(default=1, max_length=10, verbose_name='کد ملی'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.CharField(default=1, max_length=11, verbose_name='تلفن همراه'),
            preserve_default=False,
        ),
    ]

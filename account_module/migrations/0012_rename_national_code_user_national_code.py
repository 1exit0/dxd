# Generated by Django 4.2.7 on 2023-12-02 02:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0011_alter_user_first_name_alter_user_last_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='National_Code',
            new_name='national_code',
        ),
    ]
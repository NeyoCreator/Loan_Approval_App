# Generated by Django 3.2.7 on 2021-11-24 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_register', '0009_auto_20211124_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personal_details',
            old_name='image',
            new_name='image_face',
        ),
        migrations.RenameField(
            model_name='personal_details',
            old_name='title',
            new_name='title_face',
        ),
    ]

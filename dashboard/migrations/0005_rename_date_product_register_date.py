# Generated by Django 4.1.5 on 2023-03-15 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_rename_date_category_register_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Date',
            new_name='Register_Date',
        ),
    ]

# Generated by Django 4.1.5 on 2023-04-22 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_supplier_city_alter_category_register_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='Categoryid',
            new_name='Supplierid',
        ),
    ]

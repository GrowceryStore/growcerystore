# Generated by Django 4.1.5 on 2023-04-10 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_alter_category_register_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Status',
            field=models.CharField(max_length=100),
        ),
    ]

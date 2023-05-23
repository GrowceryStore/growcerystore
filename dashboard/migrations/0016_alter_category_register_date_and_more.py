# Generated by Django 4.1.5 on 2023-04-11 06:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
        migrations.AlterField(
            model_name='employeprofile',
            name='Date_Of_Join',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 4, 11)),
        ),
    ]
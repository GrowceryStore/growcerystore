# Generated by Django 4.1.5 on 2023-04-15 03:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0018_alter_category_register_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
        migrations.AlterField(
            model_name='employeprofile',
            name='Date_Of_Join',
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 4, 15)),
        ),
    ]

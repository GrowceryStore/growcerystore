# Generated by Django 4.1.5 on 2023-03-17 07:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_category_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 3, 17)),
        ),
        migrations.AlterField(
            model_name='product',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 3, 17)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Date',
            field=models.DateField(default=datetime.date(2023, 3, 17)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='Register_Date',
            field=models.DateField(default=datetime.date(2023, 3, 17)),
        ),
    ]
# Generated by Django 4.1.5 on 2023-04-21 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0026_alter_category_register_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='Productid',
        ),
        migrations.AddField(
            model_name='supplier',
            name='Categoryid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='dashboard.category'),
        ),
    ]

# Generated by Django 4.1.5 on 2023-04-17 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_order_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='Userid',
        ),
    ]

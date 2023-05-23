# Generated by Django 4.1.5 on 2023-03-15 07:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_date_product_register_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(default=datetime.date(2023, 3, 15))),
                ('Quantity', models.IntegerField()),
                ('Paid', models.FloatField()),
                ('Productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
                ('Supplierid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.supplier')),
            ],
        ),
    ]
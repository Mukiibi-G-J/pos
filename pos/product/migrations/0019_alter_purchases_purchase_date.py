# Generated by Django 4.1.10 on 2023-09-14 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0018_alter_purchases_purchase_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchases",
            name="purchase_date",
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 0, 0)),
        ),
    ]
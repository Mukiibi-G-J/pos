# Generated by Django 4.2 on 2023-05-05 14:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0015_rename_supplier_purchases_supplier"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sales",
            name="date_sold",
            field=models.DateField(),
        ),
    ]
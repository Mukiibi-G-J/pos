# Generated by Django 4.1.5 on 2023-04-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_sales_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales',
            name='stock_left',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
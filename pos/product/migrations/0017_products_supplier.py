# Generated by Django 4.1.10 on 2023-09-14 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0016_alter_sales_date_sold"),
    ]

    operations = [
        migrations.AddField(
            model_name="products",
            name="supplier",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.supplier",
            ),
        ),
    ]
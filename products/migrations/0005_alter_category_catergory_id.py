# Generated by Django 4.0.3 on 2022-04-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_options_category_catergory_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='catergory_id',
            field=models.CharField(default=1, max_length=255, unique=True),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-17 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_products_user_id_alter_products_unit_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='catergory_id',
            new_name='category_id',
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-08 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_category_image_alter_category_catergory_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='catergory_id',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='catergory_name',
            new_name='category_name',
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
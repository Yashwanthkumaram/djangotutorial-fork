# Generated by Django 4.2.19 on 2025-02-28 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_p_id_product_p_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.BinaryField(null=True),
        ),
    ]

# Generated by Django 4.2.19 on 2025-02-27 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='P_id',
            new_name='p_id',
        ),
    ]

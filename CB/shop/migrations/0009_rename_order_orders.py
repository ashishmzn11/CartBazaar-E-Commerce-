# Generated by Django 5.1.7 on 2025-04-08 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_order_delete_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]

# Generated by Django 5.1.7 on 2025-04-07 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_orders_zip_code_orders_address2_orders_zip_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='zip',
            new_name='zip_code',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
        migrations.AlterField(
            model_name='orders',
            name='address',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='city',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.CharField(max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.CharField(max_length=90),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
        migrations.AlterField(
            model_name='orders',
            name='state',
            field=models.CharField(max_length=111),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]

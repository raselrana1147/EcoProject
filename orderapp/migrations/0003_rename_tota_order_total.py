# Generated by Django 4.0.1 on 2022-03-13 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orderapp', '0002_order_orderproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='tota',
            new_name='total',
        ),
    ]

# Generated by Django 4.0.1 on 2022-03-15 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_varient_quantity_alter_varient_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variant',
            field=models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Coloe', 'Coloe'), ('SizeColor', 'SizeColor')], default='New', max_length=191),
        ),
    ]
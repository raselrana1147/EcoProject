# Generated by Django 4.0.1 on 2022-03-14 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceApp', '0002_faq'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faq',
            old_name='quation',
            new_name='question',
        ),
    ]

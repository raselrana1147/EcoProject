# Generated by Django 4.0.1 on 2022-03-15 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=191)),
                ('code', models.CharField(blank=True, max_length=191)),
            ],
        ),
    ]

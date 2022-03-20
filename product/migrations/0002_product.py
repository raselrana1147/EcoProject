# Generated by Django 4.0.1 on 2022-03-08 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191)),
                ('keyword', models.CharField(max_length=191)),
                ('image', models.ImageField(upload_to='product')),
                ('new_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('old_price', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('amount', models.IntegerField(default=0)),
                ('min_amount', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=191)),
                ('slug', models.SlugField(null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='product.category')),
            ],
        ),
    ]

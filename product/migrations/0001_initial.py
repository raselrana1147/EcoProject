# Generated by Django 4.0.1 on 2022-03-08 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=191)),
                ('keyword', models.CharField(max_length=191)),
                ('image', models.ImageField(upload_to='category')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=191)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
        ),
    ]

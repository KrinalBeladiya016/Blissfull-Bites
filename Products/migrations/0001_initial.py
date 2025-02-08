# Generated by Django 5.0.1 on 2024-02-10 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('thumbnail_image', models.ImageField(default=None, max_length=300, null=True, upload_to='categories/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=300)),
                ('product_image', models.ImageField(default=None, max_length=300, null=True, upload_to='products/')),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Products.category')),
            ],
        ),
    ]

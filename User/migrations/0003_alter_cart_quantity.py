# Generated by Django 5.0.1 on 2024-02-11 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]

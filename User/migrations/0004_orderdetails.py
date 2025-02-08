# Generated by Django 5.0.1 on 2024-02-12 11:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0003_product_quantity_desc'),
        ('User', '0003_alter_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.userdetails')),
                ('productId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.product')),
            ],
        ),
    ]

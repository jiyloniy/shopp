# Generated by Django 4.2.7 on 2023-11-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_sale_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='real_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='sale_percentage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 5.1.5 on 2025-03-04 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROOT', '0007_products_list_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_list',
            name='updated_by',
            field=models.CharField(db_column='updated_by', default='', max_length=255),
        ),
    ]

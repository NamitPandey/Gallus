# Generated by Django 5.1.5 on 2025-02-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ROOT', '0006_alter_products_list_table_comment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products_list',
            name='product_type',
            field=models.CharField(choices=[('Capsule', 'Capsule'), ('Injection', 'Injection'), ('Syrup', 'Syrup')], db_column='product_type', default='Capsule', max_length=255),
        ),
    ]

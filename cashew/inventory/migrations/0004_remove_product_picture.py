# Generated by Django 4.2.17 on 2024-12-11 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_alter_product_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='picture',
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-18 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_rename_nombre_producto_nombre_del_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_del_producto',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10),
        ),
    ]

# Generated by Django 5.1.2 on 2024-10-18 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detalles', '0001_initial'),
        ('pedidos', '0007_rename_observacion_pedido_observaciones_and_more'),
        ('preparacion', '0001_initial'),
        ('productos', '0003_alter_producto_precio_del_producto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ZonaPreparacion',
            new_name='Preparacion',
        ),
    ]

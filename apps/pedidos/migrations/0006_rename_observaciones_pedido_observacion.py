# Generated by Django 5.1.2 on 2024-10-18 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0005_remove_pedido_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pedido',
            old_name='observaciones',
            new_name='observacion',
        ),
    ]

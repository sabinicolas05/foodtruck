# Generated by Django 5.1.2 on 2024-10-18 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_remove_pedido_consumir_remove_pedido_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
    ]

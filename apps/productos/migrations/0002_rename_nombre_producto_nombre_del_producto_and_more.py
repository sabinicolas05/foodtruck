# Generated by Django 5.1.2 on 2024-10-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='nombre_del_producto',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio',
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_del_producto',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=10),
        ),
    ]

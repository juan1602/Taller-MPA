# Generated by Django 5.0.4 on 2024-05-01 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('presentacion', models.CharField(max_length=30)),
                ('fecha_creacion', models.DateTimeField()),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Cambio_stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('comentario', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField()),
                ('tipo_cambio', models.CharField(choices=[('Ingreso', 'Ingreso'), ('Egreso', 'Egreso')], max_length=7)),
                ('ref_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.productos')),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-04-24 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCombustible',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de combustible',
                'verbose_name_plural': 'Tipos de combustibles',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoLavado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de lavado',
                'verbose_name_plural': 'Tipos de lavados',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoMantenimiento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de mantenimiento',
                'verbose_name_plural': 'Tipos de mantenimientos',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Descripcion')),
            ],
            options={
                'verbose_name': 'Tipo de vehiculo',
                'verbose_name_plural': 'Tipos de vehiculos',
                'ordering': ['nombre'],
            },
        ),
    ]

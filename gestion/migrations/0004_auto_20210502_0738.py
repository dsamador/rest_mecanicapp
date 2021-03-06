# Generated by Django 3.2 on 2021-05-02 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0003_historicaltipocombustible_historicaltipomantenimiento_historicaltipovehiculo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gasolinera',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Gasolinera',
                'verbose_name_plural': 'Gasolineras',
            },
        ),
        migrations.CreateModel(
            name='Lavadero',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Lavadero',
                'verbose_name_plural': 'Lavaderos',
            },
        ),
        migrations.CreateModel(
            name='MarcaVehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, unique=True, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Taller',
                'verbose_name_plural': 'Talleres',
            },
        ),
        migrations.AlterModelOptions(
            name='tipocombustible',
            options={'verbose_name': 'Tipo de combustible', 'verbose_name_plural': 'Tipos de combustibles'},
        ),
        migrations.AlterModelOptions(
            name='tipolavado',
            options={'verbose_name': 'Tipo de lavado', 'verbose_name_plural': 'Tipos de lavados'},
        ),
        migrations.AlterModelOptions(
            name='tipomantenimiento',
            options={'verbose_name': 'Tipo de mantenimiento', 'verbose_name_plural': 'Tipos de mantenimientos'},
        ),
        migrations.AlterModelOptions(
            name='tipovehiculo',
            options={'ordering': ['nombre'], 'verbose_name': 'Tipo de vehiculo', 'verbose_name_plural': 'Tipos de vehículos'},
        ),
        migrations.RemoveField(
            model_name='historicaltipovehiculo',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='tipovehiculo',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='historicaltipovehiculo',
            name='nombre',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='tipovehiculo',
            name='nombre',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nombre'),
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del vehículo')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=10, unique=True, verbose_name='Placa')),
                ('anio', models.CharField(max_length=4, verbose_name='Año')),
                ('color', models.CharField(blank=True, max_length=40, null=True, verbose_name='Color')),
                ('tanque', models.IntegerField(verbose_name='Capacidad Tanque')),
                ('num_chasis', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Numero del Chasis')),
                ('VIN', models.CharField(blank=True, max_length=45, null=True, unique=True, verbose_name='VIN')),
                ('matricula', models.CharField(blank=True, max_length=45, null=True, unique=True, verbose_name='Matrícula')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.marcavehiculo')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestion.tipovehiculo')),
            ],
            options={
                'verbose_name': 'Vehiculo',
                'verbose_name_plural': 'Vehiculos',
            },
        ),
        migrations.CreateModel(
            name='HistoricalVehiculo',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del vehículo')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo')),
                ('placa', models.CharField(db_index=True, max_length=10, verbose_name='Placa')),
                ('anio', models.CharField(max_length=4, verbose_name='Año')),
                ('color', models.CharField(blank=True, max_length=40, null=True, verbose_name='Color')),
                ('tanque', models.IntegerField(verbose_name='Capacidad Tanque')),
                ('num_chasis', models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Numero del Chasis')),
                ('VIN', models.CharField(blank=True, db_index=True, max_length=45, null=True, verbose_name='VIN')),
                ('matricula', models.CharField(blank=True, db_index=True, max_length=45, null=True, verbose_name='Matrícula')),
                ('fecha', models.DateTimeField(blank=True, editable=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('marca', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gestion.marcavehiculo')),
                ('tipo', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='gestion.tipovehiculo')),
            ],
            options={
                'verbose_name': 'historical Vehiculo',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalTaller',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Taller',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalMarcaVehiculo',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(db_index=True, max_length=255, verbose_name='Nombre')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Marca',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLavadero',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Lavadero',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalGasolinera',
            fields=[
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('direccion', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo')),
                ('telefono', models.CharField(blank=True, max_length=15, null=True, verbose_name='Telefono')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Gasolinera',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]

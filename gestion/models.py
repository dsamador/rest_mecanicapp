from django.db.models import *
from base.models import Comunes, BaseModel, Local
from simple_history.models import HistoricalRecords
# Create your models here.


""" ##########  1  ########## +"""
class TipoLavado(Comunes):

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Tipo de lavado'
        verbose_name_plural = 'Tipos de lavados'        
    
    def __str__(self):
        return self.nombre
        

""" ##########  2  ########## +"""
class TipoMantenimiento(Comunes):

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Tipo de mantenimiento'
        verbose_name_plural = 'Tipos de mantenimientos'        
    
    def __str__(self):
        return self.nombre
        

""" ##########  3  ########## +"""
class TipoCombustible(Comunes):

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        verbose_name = 'Tipo de combustible'
        verbose_name_plural = 'Tipos de combustibles'        
    
    def __str__(self):
        return self.nombre        


""" ##########  4  ########## +"""
class TipoVehiculo(BaseModel):

    nombre = CharField('Nombre', unique=True, max_length=255, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Tipo de vehiculo'
        verbose_name_plural = 'Tipos de vehículos'        
        ordering = ['nombre'] 

    def __str__(self):
        return self.nombre


""" ##########  5  ########## """
class MarcaVehiculo(BaseModel):

    nombre = CharField('Nombre', unique=True, max_length=255, blank=False, null=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['nombre']         

    def __str__(self):
        return self.nombre


""" ##########  6  ########## """
class Lavadero(Local):
    
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Lavadero'
        verbose_name_plural = 'Lavaderos'               

    def __str__(self):
        return self.nombre
        

""" ##########  7  ########## """
class Taller(Local):
    
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Taller'
        verbose_name_plural = 'Talleres'               

    def __str__(self):
        return self.nombre
        

""" ##########  8  ########## """
class Gasolinera(Local):
    
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Gasolinera'
        verbose_name_plural = 'Gasolineras'               

    def __str__(self):
        return self.nombre
        

class Vehiculo(BaseModel):
    
    nombre = CharField('Nombre del vehículo', max_length=100, blank=False, null=False)
    modelo = CharField('Modelo', max_length=100, blank=False, null=False)
    placa = CharField('Placa', unique=True, max_length=10, blank=False, null=False)
    anio = CharField('Año', max_length=4, blank=False, null=False)    
    color = CharField('Color', max_length=40, blank=True, null=True)
    tanque = IntegerField('Capacidad Tanque', blank=False, null=False)
    num_chasis = CharField('Numero del Chasis', unique=True, max_length=100, blank=True, null=True)
    VIN = CharField('VIN', unique=True, max_length=45, blank=True, null=True)
    matricula = CharField('Matrícula', unique=True, max_length=45, blank=True, null=True)
    tipo = ForeignKey(TipoVehiculo, on_delete = PROTECT)
    marca = ForeignKey(MarcaVehiculo, on_delete = PROTECT)    
    #imagen = ImageField('Imagen del vehiculo', upload_to='vehiculos/%Y/%m/%d', height_field=None, width_field=None, max_length=None, blank=True, null=True)
    fecha = DateTimeField(auto_now_add=True)
    
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Vehiculo'
        verbose_name_plural = 'Vehiculos'               

    def __str__(self):
        return self.nombre
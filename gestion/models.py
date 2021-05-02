from django.db.models import *
from base.models import Comunes, BaseModel, Local
from simple_history.models import HistoricalRecords
# Create your models here.


""" ##########  1  ########## """
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
        

""" ##########  2  ########## """
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
        

""" ##########  3  ########## """
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


""" ##########  4  ########## """
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


""" ##########  5  ########## """
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
        

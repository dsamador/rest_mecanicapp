from django.db.models import *
from base.models import Comunes
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
        ordering = ['nombre']
    
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
        ordering = ['nombre']
    
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
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre
        

""" ##########  4  ########## """
class TipoVehiculo(Comunes):

    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Tipo de vehiculo'
        verbose_name_plural = 'Tipos de vehiculos'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre


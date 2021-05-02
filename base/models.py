from django.db.models import *

# Create your models here.
class BaseModel(Model):
    """Model definition for BaseModel."""

    # TODO: Define fields here
    id = AutoField(primary_key=True)
    state = BooleanField('Estado', default=True)
    created_date = DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    modified_date = DateField('Fecha de Modificación', auto_now=True, auto_now_add=False)    
    deleted_date = DateField('Fecha de Eliminación', auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for BaseModel."""
        abstract = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'        
        

class Comunes(BaseModel):
    
    nombre = CharField('Nombre', max_length=255, blank=False, null=False)
    descripcion = CharField('Descripcion', max_length=255, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['nombre'] 

class Local(BaseModel):
    
    nombre = CharField('Nombre', max_length=255, blank=False, null=False)
    direccion = CharField('Dirección', max_length=250, blank=True, null=True)    
    correo = CharField('Correo', max_length=100, blank=True, null=True)    
    telefono = CharField('Telefono', max_length=15, blank=True, null=True)

    class Meta:
        abstract = True
        ordering = ['nombre'] 
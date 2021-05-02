from rest_framework.routers import DefaultRouter
from gestion.api.views.tipos_viewsets import (
    TipoLavadoViewSet, TipoMantenimientoViewSet, TipoCombustibleViewSet, TipoVehiculoViewSet
)

router = DefaultRouter()

router.register(r'tipos_lavados', TipoLavadoViewSet, basename='tipos_lavados')
router.register(r'tipos_mantenimientos', TipoMantenimientoViewSet, basename='tipos_mantenimientos')
router.register(r'tipos_combustibles', TipoCombustibleViewSet, basename='tipos_combustibles')
router.register(r'tipos_vehiculos', TipoVehiculoViewSet, basename='tipos_vehiculos')

urlpatterns = router.urls
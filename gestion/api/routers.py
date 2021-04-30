from rest_framework.routers import DefaultRouter
from gestion.api.views.tipos_viewsets import TipoLavadoViewSet, TipoMantenimientoViewSet, TipoCombustibleViewSet

router = DefaultRouter()

router.register(r'tipos_lavados', TipoLavadoViewSet, basename='tipos_lavados')
router.register(r'tipos_mantenimientos', TipoMantenimientoViewSet, basename='tipos_mantenimientos')
router.register(r'tipos_combustibles', TipoCombustibleViewSet, basename='tipos_combustibles')

urlpatterns = router.urls
from rest_framework.routers import DefaultRouter
from gestion.api.views.tipos_viewsets import TipoLavadoViewSet

router = DefaultRouter()

router.register(r'tipos_lavados', TipoLavadoViewSet, basename='tipos_lavados')


urlpatterns = router.urls
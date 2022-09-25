from chamado.views import ChamadoViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register(r'chamados', ChamadoViewSet)
urlpatterns = router.urls
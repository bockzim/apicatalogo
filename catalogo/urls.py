from rest_framework.routers import DefaultRouter

from .views import FilmeViewSet, GeneroViewSet

router = DefaultRouter()
router.register('generos', GeneroViewSet)
router.register('filmes', FilmeViewSet)

urlpatterns = router.urls

from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # autenticacao
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),

    # documentacao
    path('api/schema/', SpectacularAPIView.as_view(
        permission_classes=[AllowAny], authentication_classes=[])
    ),
    path('api/docs/', SpectacularSwaggerView.as_view(
        url_name='schema', permission_classes=[AllowAny], authentication_classes=[])
    ),

    # catalogo
    path('api/', include('catalogo.urls')),
]

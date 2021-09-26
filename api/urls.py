from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)

from api.image.viewsets import ImageViewSet
from api.views import UploadView

router = routers.DefaultRouter()
router.register(r'image', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('upload/', UploadView.as_view(), name='upload'),
]

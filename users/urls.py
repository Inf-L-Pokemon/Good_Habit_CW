from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='token-obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token-refresh'),

    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
    path('<int:pk>/update/', UserUpdateAPIView.as_view(), name='user-update'),
    path('<int:pk>/delete/', UserDeleteAPIView.as_view(), name='user-delete'),
]

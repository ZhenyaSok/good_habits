from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserDeleteAPIView, \
    UserRetrieveAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = UsersConfig.name

urlpatterns = [

    path('create/', UserCreateAPIView.as_view(), name='create'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>', UserDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', UserRetrieveAPIView.as_view(), name='detail'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

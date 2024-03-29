from django.urls import path
from .api_views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

name = "accounts"

urlpatterns = [
    path('csrf/', get_csrf_token.as_view(), name='csrf'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('users/create/', UserCreateView.as_view(), name='user_create'),
    # path('users/validation/', code_validation, name='code_validation'),
    # path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    # path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    # path('users/update/password/', PasswordChangeRequest.as_view(), name='user-chagne-password-request'),
    # path('users/update/image/<int:pk>/', ProfileImageUpdateView.as_view(), name='user-update-image'),
    # path('users/change/password/', ChangePassword.as_view(), name='user-chagne-password'),
    # path('users/detail/', UserDetailView.as_view(), name='user-detail'),
    # path('users/detail/<int:pk>/', UserDetailPKView.as_view(), name='user-pk-detail'),
]

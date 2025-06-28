from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import path

from .apis import *

urlpatterns = [
    path('profile/update/', ProfileUpdateAPIView.as_view(), name='profile-update'),
    path('profile/delete/<int:id>', ProfileDeleteAPIView.as_view(), name='profile-delete'),

    path('login/', LoginAPIView.as_view(), name='log-in'),
    path('logout/', SessionLogoutAPIView.as_view(), name='log-out'),

    path('reset_password/', RequestPasswordResetView.as_view(), name='reset-password'),
    path('reset_password/confirm/', VerifyEmailView.as_view(), name='reset-password-confirm'),
]
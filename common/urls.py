from django.urls import path

from .apis import *


urlpatterns = [
    path('media-file/create/', MediaFileCreateAPIView.as_view(), name='media-file-create'),
    path('media/delete/<int:id>', MediaFileDeleteAPIView.as_view(), name='media-file-delete'),
]
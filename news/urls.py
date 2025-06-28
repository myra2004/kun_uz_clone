from django.urls import path

from .apis import *


urlpatterns = [
    # News
    path('news/craete/', NewsCreateAPIView.as_view(), name='news-create'),
    path('news/update/<int:id>/', NewsUpdateAPIView.as_view(), name='news-update'),
    path('news/list/', NewsListAPIView.as_view(), name='news-list'),
    path('news/delete/<int:id>', NewsDeleteAPIView.as_view(), name='news-delete'),

    # Category
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/delete/<int:id>', CategoryDeleteAPIView.as_view(), name='category-delete'),

    # Comment
    path('comment/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comment/list/', CommentListAPIView.as_view(), name='comment-list'),
    path('comment/delete/<int:id>', CommentDeleteAPIView.as_view(), name='comment-delete'),

    # Tag
    path('tag/create/', TagCreateAPIView.as_view(), name='tag-create'),
    path('tag/list/', TagListAPIView.as_view(), name='tag-list'),
    path('tag/delete/<int:id>', TagDeleteAPIView.as_view(), name='tag-delete'),
]
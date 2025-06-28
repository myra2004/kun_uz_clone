from django.urls import path

from .apis import *


urlpatterns = [
    # News
    path('news/craete/', NewsCreateAPIView.as_view(), name='news-create'),
    path('news/update/<pk:id>/', NewsUpdateAPIView.as_view(), name='news-update'),
    path('news/list/', NewsListAPIView.as_view(), name='news-list'),
    path('news/delete/<pk:id>', NewsDeleteAPIView.as_view(), name='news-delete'),

    # Category
    path('category/create/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('category/list/', CategoryListAPIView.as_view(), name='category-list'),
    path('category/delete/<pk:id>', CategoryDeleteAPIView.as_view(), name='category-delete'),

    # Comment
    path('comment/create/', CommentCreateAPIView.as_view(), name='comment-create'),
    path('comment/list/', CommentListAPIView.as_view(), name='comment-list'),
    path('comment/delete/<pk:id>', CommentDeleteAPIView.as_view(), name='comment-delete'),

    # Tag
    path('tag/create/', TagCreateAPIView.as_view(), name='tag-create'),
    path('tag/list/', TagListAPIView.as_view(), name='tag-list'),
    path('tag/delete/<pk:id>', TagDeleteAPIView.as_view(), name='tag-delete'),
]
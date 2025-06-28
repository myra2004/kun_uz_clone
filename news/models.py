from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Tag(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='news')
    tags = models.ManyToManyField(Tag, related_name='news', blank=True)
    default_image = models.ForeignKey('common.MediaFile', on_delete=models.SET_NULL, null=True, blank=True, related_name='default_for_news')
    is_active = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField('accounts.User', related_name='liked_news', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')


class Comment(BaseModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return self.content[:50]

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

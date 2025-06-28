from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class News(BaseModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    author_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    category_ids = models.ManyToManyField('news.Category', related_name='news')
    tags = models.ManyToManyField('news.Tag', related_name='news')
    default_image = models.ImageField(upload_to='news/', null=True, blank=True)
    image_ids = models.ManyToManyField('common.MediaFile', blank=True)
    is_active = models.BooleanField(default=True)
    views_count = models.PositiveIntegerField(default=0)
    liked_by = models.ManyToManyField('accounts.User', related_name='liked_news')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    news_ids = models.ManyToManyField('news.News', related_name='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Tag(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    news_ids = models.ManyToManyField('news.News', related_name='tags')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Comment(BaseModel):
    news_id = models.ForeignKey('news.News', on_delete=models.CASCADE)
    user_id = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    content = models.TextField()
    parent_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
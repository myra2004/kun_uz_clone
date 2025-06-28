from django.contrib import admin

from django.utils.translation import gettext_lazy as _

from news.models import News, Category, Tag, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    list_filter = ('created_at',)
    search_fields = ('title',)

    fieldsets = (
        (None, {'fields': ('title', 'content', 'author', 'category', 'tags', 'default_image')}),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'user', 'content')
    list_display_links = ('id', 'news', 'user', 'content')
    list_filter = ('created_at',)
    search_fields = ('news', 'user', 'content')
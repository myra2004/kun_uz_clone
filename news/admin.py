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
        (_("Uzbek"), {
            'fields': ('title_uz', 'content_uz')
        }),
        (_("English"), {
            'fields': ('title_en', 'content_en')
        }),
        (_("Russian"), {
            'fields': ('title_ru', 'content_ru')
        }),
        (_("Main"), {
            'fields': ('author', 'category', 'tags', 'default_image', 'slug')
        })
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    fieldsets = (
        (_("Uzbek"), {
            'fields': ('name_uz',)
        }),
        (_("English"), {
            'fields': ('name_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru',)
        }),
        (_("Main"), {
            'fields': ('slug',)
        })
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

    fieldsets = (
        (_("Uzbek"), {
            'fields': ('name_uz',)
        }),
        (_("English"), {
            'fields': ('name_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru',)
        }),
        (_("Main"), {
            'fields': ('slug',)
        })
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news', 'user', 'content')
    list_display_links = ('id', 'news', 'user', 'content')
    list_filter = ('created_at',)
    search_fields = ('news', 'user', 'content')
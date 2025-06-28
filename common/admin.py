from django.contrib import admin

from .models import MediaFile


@admin.register(MediaFile)
class MediaFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'media_type', 'file')
    list_display_links = ('id', 'media_type')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)
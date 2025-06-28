from rest_framework import serializers
from news.models import News

class NewsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = [
            'title',
            'slug',
            'content',
            'category',
            'tags',
            'default_image',
            'is_active',
        ]
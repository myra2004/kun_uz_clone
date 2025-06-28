from rest_framework import serializers

from news.models import Category

class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'name',
            'slug',
        ]
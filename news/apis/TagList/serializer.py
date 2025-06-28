from rest_framework import serializers
from news.models import Tag
class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
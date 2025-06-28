from rest_framework import serializers
from news.models import Tag
class TagCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
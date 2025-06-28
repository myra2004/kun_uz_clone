from rest_framework import serializers

from news.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'news',
            'content',
        ]
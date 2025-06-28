from rest_framework import serializers

from news.models import Comment


class CommentCreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'news',
            'content',
            'parent'
        ]
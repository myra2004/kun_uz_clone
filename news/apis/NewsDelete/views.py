from rest_framework import permissions
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from news.models import News


class NewsDeleteAPIView(DestroyAPIView):
    queryset = News.objects.all()
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
        return Response({'detail': 'This story has been deleted'}, status=status.HTTP_200_OK)
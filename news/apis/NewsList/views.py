from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializer import NewsListSerializer
from news.models import News


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
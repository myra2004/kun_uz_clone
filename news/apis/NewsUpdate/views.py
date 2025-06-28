from rest_framework import permissions
from rest_framework.generics import UpdateAPIView

from .serializer import NewsUpdateSerializer
from news.models import News


class NewsUpdateAPIView(UpdateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsUpdateSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
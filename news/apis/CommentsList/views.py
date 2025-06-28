from rest_framework import permissions
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializer import CommentListSerializer
from news.models import Comment


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(cart=self.request.user.cart)

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(serializer.data)
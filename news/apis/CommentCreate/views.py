from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from .serializer import CommentCreatSerializer
from news.models import Comment


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
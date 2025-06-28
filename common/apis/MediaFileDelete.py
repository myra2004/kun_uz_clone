from rest_framework import permissions, status
from rest_framework.generics import DestroyAPIView
from rest_framework.response import Response

from common.models import MediaFile


class MediaFileDeleteAPIView(DestroyAPIView):
    queryset = MediaFile.objects.all()
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        response = self.destroy(request, *args, **kwargs)
        return Response(status=status.HTTP_204_NO_CONTENT)
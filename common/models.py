from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MediaFile(BaseModel):
    media_type = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    news = models.ForeignKey('news.News', on_delete=models.CASCADE, related_name='media_files', null=True, blank=True)
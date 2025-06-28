from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MediaFile(BaseModel):
    media_type = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    news_ids = models.ManyToManyField('News', related_name='media_files')
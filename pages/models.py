from django.db import models
from django.utils import timezone

class Lounge(models.Model):

    image = models.ImageField(upload_to='products/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/images/기본이미지.gif'

    def __str__(self):
        return self.title
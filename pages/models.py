from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Lounge(models.Model):

    image = models.ImageField(upload_to='Lounge/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published', default=timezone.now)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    is_anonymous = models.BooleanField(default=False)


class Comments(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Lounge/', blank=True, null=True)
    content_list = models.ForeignKey(Lounge, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    heart = models.PositiveIntegerField(default=0)
    modify_date = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    
    
class Reply(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Lounge/', blank=True, null=True)
    content_list = models.ForeignKey(Lounge, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    heart = models.PositiveIntegerField(default=0)
    modify_date = models.DateTimeField(auto_now=True)
    parent_comment = models.ForeignKey(Comments, null=True, blank=True, on_delete=models.CASCADE, related_name='reply_replies')



    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/images/기본이미지.gif'

    
    def __str__(self):
       
        return f'{self.author} - {self.content}'
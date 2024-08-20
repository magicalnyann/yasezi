from django.db import models
from django.contrib.auth.models import User

class MainContent(models.Model):
    category = models.CharField(max_length=100, default='default_category')
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.BigIntegerField(default=0)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class RecommProduct(models.Model):
    category = models.CharField(max_length=100, default='default_category')
    image = models.ImageField(upload_to='recomm_products/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.BigIntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.content_list.image:
            return self.content_list.image.url
        return '/static/images/기본이미지.gif'

    def __str__(self):
        return f"Comment by {self.author.username} on {self.content_list.title}"
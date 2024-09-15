from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    address_detail = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    breed = models.CharField(max_length=50, blank=True, null=True)
    cat_name = models.CharField(max_length=50, blank=True, null=True)
    #포인트 필드 admin 이외 관리 금지
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

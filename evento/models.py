from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random


class Evento(models.Model):
    date = models.DateField(auto_now_add=True)
    # 메인 이미지
    main_event = models.ImageField(upload_to='evento/', blank=True, null=True)
    #이벤트 이미지 및 팝업
    nyan_ncat = models.FileField(upload_to='evento/', blank=True, null=True)
    pok_pal = models.FileField(upload_to='evento/', blank=True, null=True)
    popup_1 = models.FileField(upload_to='evento/', blank=True, null=True)
    popup_2 = models.FileField(upload_to='evento/', blank=True, null=True)

    def __str__(self):
        return f"Evento on {self.date}"



class UserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    points_awarded = models.IntegerField()

    def __str__(self):
        return f"User {self.user.username} received {self.points_awarded} points for Evento on {self.date}"

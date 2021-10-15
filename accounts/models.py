from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):   # 추가
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'id={self.id}, user_id={self.user.id}, college={self.college}, major={self.major}'

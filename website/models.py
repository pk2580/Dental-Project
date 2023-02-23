from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Messageorm(models.Model):
    name=models.CharField(max_length=256)
    message=models.CharField(max_length=256)
    email=models.ForeignKey(User, on_delete=models.CASCADE,)
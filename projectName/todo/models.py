from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoModel(models.Model):  
  content = models.CharField(max_length=200)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
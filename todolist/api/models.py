from django.db import models
import datetime
import django.utils.timezone as timezone

# Create your models here.

class Task(models.Model):#1

    title =models.CharField(max_length=256)
    content =models.TextField()
    priority_level=models.SmallIntegerField()
    status=models.SmallIntegerField(default=0,blank=True)
    create_time=models.DateTimeField(auto_now_add=True,blank=True)
    expire_time =models.DateField(blank=True,null=True)
    last_modify_time=models.DateTimeField(auto_now = True)

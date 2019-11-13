from django.db import models

# Create your models here.

class Question(models.Model):#问题描述和发布时间
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date publisthed')

class Choice(models.Model):# 两个字段，包括选项描述和当前票数
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(max_length=200)

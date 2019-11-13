from rest_framework import serializers
from .models import Task

#2
class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id','title', 'content', 'priority_level', 'status','expire_time','last_modify_time')
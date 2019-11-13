·from rest_framework import mixins,viewsets
from rest_framework.views import Response
from django.views.generic import View
from .models import Task
from .serializers import TaskSerializers
from django.shortcuts import render


#3
# Create your views here.
class TaskListView(mixins.ListModelMixin,
                  viewsets.GenericViewSet,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                ):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers




class IndexVIew(View):
    def get(self,request):
        return render(request,'index.html')

from rest_framework import generics, status
from .models import Task
from .serializers import TaskSerializer

class TasksAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ['customer', 'status']
    ordering_fields = ['assigned_to', 'customer']
    ordering = ['assigned_to', 'customer']
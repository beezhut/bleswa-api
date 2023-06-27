from django.urls import path
from .views import TasksAPIView

urlpatterns = [
    path('tasks', TasksAPIView.as_view(), name='tasks'),
]
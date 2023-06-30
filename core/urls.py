from django.urls import path
from .views import *

urlpatterns = [
    path('tasks', TasksList.as_view(), name='tasks'),
    path('tasks/<str:pk>/', TaskDetail.as_view()),
    path('activities', ActivityAPIView.as_view(), name='activities'),
]
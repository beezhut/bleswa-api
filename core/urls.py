from django.urls import path
from .views import *

urlpatterns = [
    path('tasks/', TasksList.as_view(), name='tasks'),
    path('task/<str:pk>/', TaskDetail.as_view()),
    path('activities/', ActivityList.as_view(), name='activities'),
    path('activity/<str:pk>/', ActivityDetail.as_view()),
    path('loans/', LoanList.as_view(), name='activities'),
    path('loan/<str:pk>/', LoanDetail.as_view()),
]
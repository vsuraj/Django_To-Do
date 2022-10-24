from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('task/new', task_list, name='task_list'),
    path('task/edit/<int:pk>', task_edit, name='task_edit'),
    path('task/delete/<int:pk>', task_delete, name='task_delete'),
]
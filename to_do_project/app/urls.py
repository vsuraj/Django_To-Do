from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('', index, name='index'),
    path('list_task', list_task, name='list_task'),
    path('edit_task/<int:id>',edit_task, name='edit_task'),
    path('delete_task/<int:id>',delete_task, name='delete_task'),
]
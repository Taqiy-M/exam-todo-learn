from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_index),
    path('delete-todo/<int:a>/', delete_todo)
]

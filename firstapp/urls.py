from django.urls import path
from .views import TodoList,TodoCreate

urlpatterns = [
  path('list/', TodoList),
  path('create/', TodoCreate),
]
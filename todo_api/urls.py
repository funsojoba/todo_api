from django.urls import path
from .views import ListTodo, SingleTodo


urlpatterns = [
    path('', ListTodo.as_view(), name='list todo'),
    path('<str:pk>/', SingleTodo.as_view(), name='single todo')
]

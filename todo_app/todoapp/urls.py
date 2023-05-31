from django.urls import path

from todo_app.todoapp.views import index

urlpatterns = [
    path('', index, name='index'),
]

# from django.contrib import admin 
# from django.urls import path 
# from .views import IndexView 
# from . import views

# urlpatterns = [
#     path('', IndexView.as_view(), name='todolist'),
# ]

from django.urls import path
from .views import IndexView, AddTodoView, EditTodoView, DeleteTodoView

app_name = 'todo'

urlpatterns = [
    path('', IndexView.as_view(), name='todolist'),
    path('add/', AddTodoView.as_view(), name='add_todo'),
    path('<int:pk>/edit/', EditTodoView.as_view(), name='edit_todo'),
    path('<int:pk>/delete/', DeleteTodoView.as_view(), name='delete_todo'),
]

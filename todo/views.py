# todo/views.py

from django.shortcuts import render
from .models import TodoList, TodoList_files, TodoList_images
from django.views import generic
from django.views.generic import ListView

# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'to_do_list'
    template_name = 'todo/todo-lists.html'  # 템플릿 파일 경로

    def get_queryset(self):
        return TodoList.objects.all()

class TodoListView(ListView):
    model = TodoList
    template_name = 'todo/todo_list.html'  # 템플릿 파일 경로
    context_object_name = 'todos'

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from .models import TodoList

class IndexView(ListView):
    context_object_name = 'to_do_list'
    template_name = 'todo/todo-lists.html'

    def get_queryset(self):
        return TodoList.objects.all()

class AddTodoView(View):
    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        date_deadline = request.POST.get('date_deadline')
        TodoList.objects.create(name=name, description=description, date_deadline=date_deadline)
        return redirect('todo:todolist')

class EditTodoView(View):
    def get(self, request, pk):
        todo = get_object_or_404(TodoList, pk=pk)
        return render(request, 'todo/todo_list.html', {'todo': todo})

    def post(self, request, pk):
        todo = get_object_or_404(TodoList, pk=pk)
        todo.name = request.POST.get('name')
        todo.description = request.POST.get('description')
        todo.date_deadline = request.POST.get('date_deadline')
        todo.save()
        return redirect('todo:todolist')

class DeleteTodoView(View):
    def post(self, request, pk):
        todo = get_object_or_404(TodoList, pk=pk)
        todo.delete()
        return redirect('todo:todolist')


from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import TodoItem        
# Create your views here.
def todolist(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo.html', {'todos': todos})

def create_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        TodoItem.objects.create(title=title, description=description)
        return redirect("todolist")
    return render(request, 'todo_form.html') 

def update_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description', '')
        todo.completed = request.POST.get("completed") == 'on'
        todo.save()
        return redirect("todolist")
    
    return render(request, 'todo_form.html', {'todo': todo})

def delete_todo(request, id):
    todo = get_object_or_404(TodoItem, id=id)
    todo.delete()
    return redirect("todolist")
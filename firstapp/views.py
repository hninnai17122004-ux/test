from django.shortcuts import render
from .models import TodoModel

# Create your views here.
def TodoList(request):
    todo = TodoModel.objects.all()
    context = {
        'todo':todo
    }

    return render(request, 'todo_list.html',context)

def TodoCreate(request):
    return render(request, 'todo_create.html')

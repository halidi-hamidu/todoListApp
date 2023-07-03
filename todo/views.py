from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.
def indexpage(request):
    todo_title=Todo.objects.all()
    context ={
        "todo_titles": todo_title,
    }
    if request.method == "POST":
        new_object=Todo(
            title=request.POST['title'] 
        )
        new_object.save()
        return redirect("/")
    return render (request, 'todo/index.html', context)
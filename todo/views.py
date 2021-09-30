from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TodoForm
from .models import Todo


@login_required
def index(request):
    context = {
        'todos': request.user.todo_set.all().order_by('due_date'),
    }
    return render(request, 'todo/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo:index')
    else:
        form = TodoForm()

    context = {
        'form': form,
    }

    return render(request, 'todo/form.html', context)


@login_required
def delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if todo.user == request.user:
        todo.delete()
    return redirect('todo:index')

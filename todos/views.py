from django.shortcuts import render, redirect, get_object_or_404

from .forms import TodoForm
from .models import Todo

from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):

    # if you want import some values in request, use request.session
    # visit_num = request.session.get('visit_num', 0)

    # request.session['visit_num'] = visit_num + 1
    # request.session.modified = True

    # context = {
    #     'visit_num': visit_num
    # }

    todos = request.user.todo_set.all().order_by('due_date')

    context = {
        'todos': todos,
    }

    return render(request, 'todos/index.html', context)


@login_required
def create(request):

    if request.method == 'POST':
        form = TodoForm(request.POST)

        if form.is_valid():

            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()

            return redirect('todos:index')
    else:
        form = TodoForm()

    context = {
        'form': form,
    }

    return render(request, 'todos/form.html', context)


@login_required
def delete(request, todo_id):

    todo = get_object_or_404(Todo, id=todo_id)

    if todo.user == request.user:
        todo.delete()

    return redirect('todos:index')

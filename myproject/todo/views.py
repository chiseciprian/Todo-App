import httplib2
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from datetime import datetime, timezone
from django.core.mail import send_mail
from django.conf import settings


from .models import Todo
from .forms import TodoForm


def index(request):
    todo_list = Todo.objects.order_by('date')

    for todo in todo_list:
        if todo.date.date() < datetime.now().date():
            todo.complete = True
            todo.save()

    time = datetime.now()

    form = TodoForm()

    context = {'todo_list': todo_list, 'form': form, 'time': time}


    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)

    print(request.POST['text'], request.POST['date'])

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'], date=form.cleaned_data['date'])
        new_todo.save()
        subject = "Time for ToDo's :)"
        message = ' Your ToDo has a new event added. Checkout ToDo app :)'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['ADD RECIPIENT EMAIL', ]
        result = send_mail(subject, message, email_from, recipient_list)
        print(result)

    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')


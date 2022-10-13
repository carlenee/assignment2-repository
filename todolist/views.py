import datetime
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Task
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from datetime import date
from django.views.decorators.csrf import csrf_exempt

@login_required(login_url="/todolist/login/")
# Create your views here.
def show_todolist(request):
    # user_name = User.objects.get(username=request.user)   
    if request.user.is_authenticated:
        user_name = request.user.username 
        data_tasklist = Task.objects.filter(user= request.user)
        context = {'todolist': data_tasklist, 
                    'username': user_name,
                    # 'last_login': request.COOKIES['last_login']
        }
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            # response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

def create_task(request):
    user_name = User.objects.get(username=request.user)    
    form = TaskForm()
    new_task = None
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    context = {'form': form}
    return render(request, 'create-task.html', context)
@csrf_exempt
def mark_as_finished(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.is_finished = not(task.is_finished)
    task.save(update_fields = ['is_finished'])
    return JsonResponse({"Message": "Task Updated"},status=200)

# def delete_task(request, id):
#     task = Task.objects.get(id=id)
#     task.delete()
#     return HttpResponseRedirect(reverse("todolist:show_todolist"))

def show_todolist_json(request):
    task = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", task), content_type="application/json")

def create_task_ajax(request):
     if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        user = request.user
        date = datetime.datetime.now()
        is_finished = False
        item = Task(title=title, description=description, user=user, date=date, is_finished=is_finished)
        item.save()
        return JsonResponse({"Message": "Task Success"},status=200)

@csrf_exempt
def delete_task(request, id):
    task = Task.objects.get(user=request.user, id=id)
    task.delete()
    return JsonResponse({"Message": "Task Deleted"},status=200)


import json
from django.urls import path
from todolist.views import register
from todolist.views import login_user,delete_task, show_todolist_json, create_task_ajax
from todolist.views import logout_user, show_todolist, create_task, mark_as_finished

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name = 'show_todolist'),
    path('register/', register, name= 'register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('mark-as-finished/<int:id>/', mark_as_finished, name='mark_as_finished'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('json/', show_todolist_json, name='show_todolist_json'),
    path('add/', create_task_ajax, name = 'create_task_ajax'),
]

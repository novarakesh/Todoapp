from django.contrib import admin
from django.urls import path,include
from . import views   

urlpatterns = [
    path('',views.todolist,name="todolist"),
    path('create/',views.create_todo,name="create_todo"),
    path('update/<int:id>/',views.update_todo,name="update_todo"),
    path('delete/<int:id>/',views.delete_todo,name="delete_todo"),
]

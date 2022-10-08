from django.urls import path

from todo_api import views

urlpatterns = [
    path('addtask/', views.AddTask.as_view(), name="add-new-task")
]
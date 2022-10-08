from django.urls import path

from todo_api import views

urlpatterns = [
    path('task/', views.AddTask.as_view(), name="add-new-task"),
    path('task/<task_id>', views.AddTask.as_view(), name="add-new-task"),
    path('tasks/', views.TaskList.as_view(), name="add-new-task")
]
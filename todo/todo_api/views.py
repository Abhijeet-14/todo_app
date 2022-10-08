
import inspect
import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from todo_api.task.controller import add_new_task_controller, get_task_list_controller, get_task_controller

# Create your views here.
class AddTask(APIView):

    def get(self, request, task_id):
        """Get Single Task"""
        return get_task_controller(request, task_id)

    def post(self, request):
        """Add new task"""
        return add_new_task_controller(request)

class TaskList(APIView):

    def get(self, request):

        return get_task_list_controller(request)

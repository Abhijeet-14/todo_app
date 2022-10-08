import inspect
import uuid

from rest_framework.response import Response
from rest_framework import status

from common.common_function import custom_logger, get_func_name
from common.formatted_response import formatted_response
from exceptions.CustomExceptions import formatted_exception
from todo_api.task.service import add_new_task, get_task_list, get_task

logger = custom_logger(__name__)


def add_new_task_controller(request):
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        result = add_new_task(request)

        logger.info(f"Exit : {func_name}")

        return formatted_response(result, status_code=201, func_name=func_name)

    except Exception as err:
        return formatted_exception(err, func_name=func_name)

def get_task_controller(request, task_id):
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        result = get_task(request, task_id)

        logger.info(f"Exit : {func_name}")

        return formatted_response(result, status_code=200, func_name=func_name)
    except Exception as err:
        return formatted_exception(err, func_name=func_name)    

def get_task_list_controller(request):
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter : {func_name}")

        result = get_task_list(request)

        logger.info(f"Exit : {func_name}")

        return formatted_response(result, status_code=200, func_name=func_name)
    except Exception as err:
        return formatted_exception(err, func_name=func_name)
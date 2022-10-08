import inspect

from common.common_function import custom_logger, get_func_name
from common.serializer_helper import check_serializer
from common.CustomSaveToDB import validate_before_save_to_db

from exceptions.CustomExceptions import CustomApiException

from .serializer import CreateNewTaskSerializer, SingleTaskSerializer, TaskModelSerializer
from .models import Task

logger = custom_logger(__name__)


def add_new_task(request):
    """Add new task service"""
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter: {func_name}")

        request_serializer = CreateNewTaskSerializer(data=request.data)

        check_serializer(request_serializer)

        validated_data = dict(request_serializer.validated_data)

        logger.info("Creating Model Instance : Task")
        instance = Task(
            title = validated_data['title'],
            description = validated_data['description'],
            help = validated_data['help'],
            priority = validated_data['priority'],
        )

        validate_before_save_to_db(instance)

        logger.info("Model serializer to convert to dict : Task")
        response_serilizer = TaskModelSerializer(instance, many=False)

        response_data = response_serilizer.data

        logger.info(f"Exit: {func_name}")
        return response_data
    except Exception as err:
        logger.error(f"Exit : {func_name} :: Error occured : {str(err)}")
        raise err

def get_task(request, task_id):
    """Get List of all task per pagination"""
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter: {func_name}")

        request_serilizer = SingleTaskSerializer(data={"task_id": task_id})

        check_serializer(request_serilizer)
        validated_data = request_serilizer.data

        logger.info(f"Getting single task by task_id : {task_id}")
        task_instance = Task.objects.get(task_id=validated_data['task_id'])
        ## Input Error: task doesn't exist for task_id
        logger.info(task_instance)

        response_serilizer = TaskModelSerializer(task_instance, many=False)
        response_data = response_serilizer.data

        logger.info(f"Exit: {func_name}")
        return response_data
    except Exception as err:
        logger.error(f"Exit : {func_name} :: Error Occured : {str(err)}")
        raise err


def get_task_list(request):
    """Get List of all task per pagination"""
    func_name = get_func_name(inspect.currentframe())
    try:
        logger.info(f"Enter: {func_name}")

        list_instance = Task.objects.all()

        response_serilizer = TaskModelSerializer(list_instance, many=True)

        response_data = response_serilizer.data

        logger.info(f"Exit: {func_name}")
        return response_data
    except Exception as err:
        logger.error(f"Exit : {func_name} :: Error Occured : {str(err)}")
        raise err

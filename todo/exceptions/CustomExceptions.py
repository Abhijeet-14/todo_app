import logging
import uuid
import inspect

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import exception_handler

from common.common_function import status_switch, custom_logger

logger = custom_logger(__name__)


class CustomApiException(APIException):
    """Custom Exceptopms tp raise as per our need"""

    # public fields
    detail = None
    status_code = None

    # constructor
    def __init__(self, message, status_code):
        
        # override public fields
        CustomApiException.detail = message
        CustomApiException.status_code = status_code


def formatted_exception(error, others=None, func_name=""):
    """
    Exception format for an api
    error: error message
    others: dict with key-value
    """
    err_ref = uuid.uuid4()
    logger.error(f"{func_name} {str(error)} :: [err_ref = {err_ref}]")
    try:
        status_code = status_switch(error.status_code)
    except Exception:
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    message = {"error": str(error), "isTrue": False, "err_ref": str(err_ref)}

    if others is not None:
        message.update(others)

    return Response(message, status=status_code)


def custom_exception_handler(exec, context):
    """
    exec: exception
    context: context
    """
    response = exception_handler(exec, context)

    if response is not None:
        response.data["status_code"] = response.status_code

        response.data["message"] = response.data["detail"]

        del response.data["detail"]

    return response

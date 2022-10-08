import uuid
from rest_framework.response import Response

from common.common_function import custom_logger, status_switch

logger = custom_logger(__name__)


def formatted_response(response, status_code=200, others=None, func_name=None):
    """
    Exception format for an api
    error: error message
    others: dict with key-value
    """
    response_ref = uuid.uuid4()
    logger.info(f"{func_name} API request Success :: [response_ref = {response_ref}]")

    status_response = status_switch(status_request=status_code)

    result = {"result": response, "isTrue": True, "response_ref": response_ref}

    if others is not None:
        result.update(others)

    return Response(result, status=status_response)



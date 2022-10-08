import inspect
import logging
from rest_framework import status


def custom_logger(name):
    """
    name: function name
    returns logger per a function
    """
    return logging.getLogger(name)


def get_func_name(current_frame):
    return f"{current_frame.f_code.co_name}()"


def status_switch(status_request):
    """
    status_request: INT
    returns status code as per rest_framework.status
    """

    logger = custom_logger(__name__)
    func_name = get_func_name(inspect.currentframe())

    swtich = {
        200: status.HTTP_200_OK,
        201: status.HTTP_201_CREATED,
        202: status.HTTP_202_ACCEPTED,
        300: status.HTTP_300_MULTIPLE_CHOICES,
        400: status.HTTP_400_BAD_REQUEST,
        401: status.HTTP_401_UNAUTHORIZED,
        403: status.HTTP_403_FORBIDDEN,
        404: status.HTTP_404_NOT_FOUND,
        405: status.HTTP_405_METHOD_NOT_ALLOWED,
        500: status.HTTP_500_INTERNAL_SERVER_ERROR,
        503: status.HTTP_503_SERVICE_UNAVAILABLE,
    }

    status_response = swtich.get(status_request, status.HTTP_500_INTERNAL_SERVER_ERROR)

    logger.info(
        f"Exit : {func_name} for status_request: {status_request} :: status_response: {status_response}"
    )

    return status_response

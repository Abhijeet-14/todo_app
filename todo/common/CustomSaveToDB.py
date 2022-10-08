import logging

from django.core.exceptions import ValidationError
from exceptions.CustomExceptions import CustomApiException
from rest_framework import status

import inspect
from common.common_function import custom_logger, get_func_name
logger = custom_logger(__name__)


def validate_before_save_to_db(instance):
    """Validate Model data before save them into respt. table
    :instance - instance of the Model
    """
    func_name = get_func_name(inspect.currentframe())#"validate_before_save_to_db()"
    table_name = instance._meta
    try:
        logger.info(
            f"Enter {func_name}: Validation Check starts for table :: {table_name}"
        )
        instance.full_clean()
    except ValidationError as error:
        logger.error(
            f"Error {func_name}: Error while saving to Table :: {table_name} :: {error}"
        )
        raise CustomApiException(
            f"Error while saving to DB: {error}", status.HTTP_400_BAD_REQUEST
        )
    else:
        logger.info(
            f"Exit {func_name}: Validation is Ok!, Saving to table :: {table_name}"
        )

        try:
            instance.save()

        except Exception as error:
            logger.info(
                f"Error occured: .save() is not working :: [{error}]"
            )
            raise CustomApiException(
                "Error while saving to DB, either Network issue or Db is closed",
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

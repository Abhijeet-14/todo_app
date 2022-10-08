import logging

from django.core import validators
from django.core.exceptions import ValidationError

import inspect
from common.common_function import custom_logger, get_func_name
logger = custom_logger(__name__)


def validate_email(email, error_list):
    """Validate Email"""
    try:
        logger.debug("Start: Email validation")
        validators.validate_email(email)

        logger.debug("End: Email validation :: Success")
    except ValidationError as error:
        formattedValidationError(error, error_list, "Email", email)


def validate_URL(URL, error_list):
    """Validate URL"""
    try:
        logger.debug("Start: URL validation")

        validate_url = validators.URLValidator()
        validate_url(URL)

        logger.debug("End: URL validation :: Success")
    except ValidationError as error:
        formattedValidationError(error, error_list, "URL", URL)


def validate_title(news_title, error_list):
    """Validate News title"""
    try:
        logger.debug("Start: News Title validation")
        logger.debug("End: News Title validation :: Success")
        pass
    except ValidationError as error:
        formattedValidationError(error, error_list, "News Title", news_title)


def validate_content(news_content, error_list):
    "Validate News Content"
    try:
        logger.debug("Start: News Content validation")
        logger.debug("End: News Content validation :: Success")
        pass
    except ValidationError as error:
        formattedValidationError(error, error_list, "News Content", news_content)


def formattedValidationError(error, error_list, type, value):
    """Formatted Validation Error"""
    error = error.message

    logger.error(f"Error: {type} validation :: {error} :: {value}")
    error_list.append(error)


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose-file": {
            "format": "[{levelname}] [{asctime}] [L{lineno}] [{name}.{funcName}s()] - {message}",
            "style": "{",
        },
        "basic": {
            "format": "[{levelname}] [{name}.{funcName}s()] [L:{lineno}] {message}",
            "style": "{",
        },
        "simple-console": {
            "format": "[{levelname}] [L{lineno}] [{name}.{funcName}s()] [{name}] - {message}",
            "style": "{",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler", 
            "level": "DEBUG",
            "formatter": "simple-console"
        },
        "all": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "./todo/logs/all.log",
            "formatter": "verbose-file",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "./todo/logs/error.log",
            "formatter": "basic",
        },
    },
    "loggers": {
        "todo_api": {
            "handlers": ["all", "error"],
            "level": "DEBUG",
            "propagete": True,
        },
        "common": {
            "handlers": ["all"],
            "level": "INFO",
            "propagete": True,
        },
        "exceptions": {
            "handlers": ["all"],
            "level": "INFO",
            "propagete": True,
        },
        "root": {"handlers": ["console"], "level": "DEBUG"},
        "django": {
            "handlers": ["all", "error"],
            # "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
            "level": "INFO",
            "propagete": True,
        },
        "django.utils.autoreload": {
            "level": "CRITICAL",
        },
    },
    
}


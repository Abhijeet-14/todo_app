
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
            "format": "[{levelname}] [L{lineno}] [{name}.{funcName}s()] - {message}",
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
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "filename": "./todo/logs/all.log",
            "formatter": "verbose-file",
        },
        "error": {
            "level": "ERROR",
            "class": "logging.FileHandler",
            "filename": "./todo/logs/error.log",
            "formatter": "verbose-file",
        },
    },
    "loggers": {
        "todo_api": {
            "handlers": ["all", "error"],
            "level": "DEBUG",
        },
        "common": {
            "handlers": ["all", "error"],
            "level": "DEBUG",
        },
        "exceptions": {
            "handlers": ["all", "error"],
            "level": "DEBUG",
        },
        "root": {"handlers": ["console"], "level": "DEBUG"},
        "django": {
            "handlers": ["all", "error"],
            "level": "INFO",
            "propagete": True,
        },
        "django.utils.autoreload": {
            "level": "CRITICAL",
        },
    },
    
}


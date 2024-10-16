# Задание 4
import logging
import logging.config

dict_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'file_debug': {
            'class': 'logging.FileHandler',
            'level': 'DEBUG',
            'formatter': 'default',
            'filename': 'calc_debug.log',
            'encoding': 'utf-8',
        },
        'file_error': {
            'class': 'logging.FileHandler',
            'level': 'ERROR',
            'formatter': 'default',
            'filename': 'calc_error.log',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['file_debug', 'file_error'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}

# Задание 7
import logging


class AsciiFilter(logging.Filter):
    def filter(self, record):
        return 1 if record.message.encode().isascii() else 0

dict_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)s | %(message)s"
        }
    },
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calculate.log",
            "encoding": "utf-8"
        },
        "timed": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "calculate.log",
            "when": "H",
            "interval": 10,
            "backupCount": 0,
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "Calculate": {
            "level": "DEBUG",
            "handlers": ["file"],
            "filter": AsciiFilter
        }
    },

}

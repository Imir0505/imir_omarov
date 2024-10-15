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

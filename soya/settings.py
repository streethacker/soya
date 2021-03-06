# -*- coding: utf-8 -*-

ENV = 'dev'
DEBUG = True

SECRET_KEY = 'A0Zj98l/3yX HZX~R!jmNLWX/,P?K'

API_KEY = 'BE46f91b984e525e7f65b63bd9d86caf'
API_URI = 'http://api.map.baidu.com/telematics'
API_VERSION = 'v3'

OUTPUT_JSON_FORMATTER = True

LOGGING_SETTINGS = {
    'version': 1,

    'disable_existing_loggers': False,

    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },

    'loggers': {
        'agera': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'INFO',
        },
    },

    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'general',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'general',
            'filename': '/var/log/agera/agera.log',
        },
    },

    'formatters': {
        'general': {
            'format': '%(asctime)s %(levelname)-6s [%(name)s][%(process)d]'
                      ' %(message)s'
        },
        'detail': {
            'format': '%(asctime)s %(levelname)-6s [%(name)s][%(process)d]'
                      '[%(pathname)s: %(lineno)d]'
                      ' %(message)s',
        },
    }
}


MYSQL_SETTINGS = {
    'user': 'root',
    'passwd': 'root',
    'host': 'localhost',
    'port': '3306',
    'database': 'soya',
}

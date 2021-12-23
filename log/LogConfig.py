

from logging.config import dictConfig

LOGGER = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(name)s: %(message)s'
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'default',
            'filename': 'app.log',
            'level': 'INFO',
            'maxBytes': 524288,
            'backupCount': 3,
            'delay': True,
            'encoding': 'utf-8'
        },
        'stream':{
            'class': 'logging.StreamHandler',
            'formatter': 'default',
            'level': 'INFO'
        }
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file','stream']
    }
}

dictConfig(LOGGER)
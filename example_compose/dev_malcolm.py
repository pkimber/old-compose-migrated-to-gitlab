# -*- encoding: utf-8 -*-
import socket
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'temp.db',                               # Or path to database file if using sqlite3.
        'USER': '',                               # Not used with sqlite3.
        'PASSWORD': '',                           # Not used with sqlite3.
        'HOST': '',                              # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                                          # Set to empty string for default. Not used with sqlite3.
    }
}

MIDDLEWARE_CLASSES += MIDDLEWARE_CLASSES + (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS += (
    #'django.contrib.formtools',
    'django_extensions',
    'debug_toolbar',
)

INTERNAL_IPS = ['127.0.0.1']

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'localhost',
    '::1',
    socket.gethostbyname(socket.gethostname()),
]

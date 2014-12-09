# Development environment settings

from .default import *

DEBUG = True

INSTALLED_APPS = DEFAULT_APPS + (
    'game',
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES + ()
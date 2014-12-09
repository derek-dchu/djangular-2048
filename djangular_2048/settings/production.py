# Production environment settings

from os import environ

from .default import *

DEBUG = False

INSTALLED_APPS = DEFAULT_APPS + (
	'game',
	)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES + ()

#### SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = environ.get('SECRET_KEY')
#### END SECRET CONFIGURATION

#### ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']
#### END ALLOWED HOST CONFIGURATION

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
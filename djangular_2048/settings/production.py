# Production environment settings

from os import environ

from .default import *

DEBUG = False

INSTALLED_APPS = DEFAULT_APPS + (
    'game',

    # The Django sites framework is required by allauth
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.twitter',
    )

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES + ()

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (

    # allauth specific context processors
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

AUTHENTICATOIN_BACKENDS = (
    'django.contrib.auth.backend.ModelBackend'

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

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

SITE_ID = 2

# Allauth settings
# auth and allauth settings
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'oauth2',  # instead of 'js_sdk'
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.2'
    }
}

# Email server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'investnotice@gmail.com'
EMAIL_HOST_PASSWORD = 'investnotice123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@djangular-2048.com'
# Development environment settings

from .default import *

DEBUG = True

INSTALLED_APPS = DEFAULT_APPS + (
    'django.contrib.sites',

    'account',
    'social.apps.django_app.default',
    'bootstrap3',

    'game',
)

MIDDLEWARE_CLASSES = DEFAULT_MIDDLEWARE_CLASSES + (
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'account.context_processors.account',

    'social.apps.django_app.context_processors.backends',
   'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'account.auth_backends.EmailAuthenticationBackend',

    'social.backends.facebook.FacebookOAuth2',
    'social.backends.google.GoogleOAuth2',
    'social.backends.twitter.TwitterOAuth',
)


#### Python-Social-Auth Settings
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

LOGIN_REDIRECT_URL = '/'


#### Python-User-Accounts settings
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True


SITE_ID = 2
#### Setup Email server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'investnotice@gmail.com'
EMAIL_HOST_PASSWORD = 'investnotice123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@djangular-2048.com'


try:
    from .local_settings import *
except ImportError:
    import sys, traceback
    sys.stderr.write("Warning: Can't find the file 'local_settings.py' in the directory containing {}. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n".format(__file__))
    sys.stderr.write("\nFor debugging purposes, the exception was:\n\n")
    traceback.print_exc()
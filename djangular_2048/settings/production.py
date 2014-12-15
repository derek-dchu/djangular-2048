# Production environment settings

from os import environ

from .default import *

DEBUG = False

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
    'social.apps.django_app.middleware.SocialAuthExceptionMiddleware',
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

#### Python-Social-Auth Settings
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['username', 'first_name', 'email']

LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Twitter
SOCIAL_AUTH_TWITTER_KEY = environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = environ.get('SOCIAL_AUTH_TWITTER_SECRET')


#### Python-User-Accounts settings
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = True


SITE_ID = 1
#### Setup Email server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'investnotice@gmail.com'
EMAIL_HOST_PASSWORD = 'investnotice123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'admin@djangular-2048.com'
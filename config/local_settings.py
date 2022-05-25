import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '#06gw0pdt5b=%^p29@!rqwf12vvqfqwd12gasdqwv*1-aopwl8gs'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFIELS_DIRS = (
    [STATIC_DIR],
)


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

AUTH_USER_MODEL = "accounts.CustomUser"


SESSION_TIMEOUT_REDIRECT = '/login'

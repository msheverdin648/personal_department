import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '#06gw0pdfq3d13gh24qfgf31r3r@$!51t11shrgeaf-t9&v*1-aopwl8gs'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'login'

AUTH_USER_MODEL = "accounts.CustomUser"

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# django/mysite/config/settings/production.py
import os
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['.railway.app']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-production-secret-key')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ["PGDATABASE"],
        'USER': os.environ["PGUSER"],
        'PASSWORD': os.environ["PGPASSWORD"],
        'HOST': os.environ["PGHOST"],
        'PORT': os.environ["PGPORT"],
    }
}

# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
# STATIC_URL = '/static/'

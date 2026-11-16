import dj_database_url
import os
from .common import *

DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['.vercel.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['TIDB_DB_NAME'],
        'HOST': os.environ['TIDB_HOST'],
        'PORT': os.environ.get('TIDB_PORT', '4000'),
        'USER': os.environ['TIDB_USER'],
        'PASSWORD': os.environ['TIDB_PASSWORD'],
    
    }
}

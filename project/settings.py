import os

from environs import Env

env = Env()
env.read_env()

with env.prefixed("BANK_BASE_"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': env('HOST'),
            'PORT': '5434',
            'NAME': env('NAME'),
            'USER': env('USER'),
            'PASSWORD': env('PASSWORD'),
        }
    }

INSTALLED_APPS = ['datacenter']

with env.prefixed("CHECKPOINT_"):
    SECRET_KEY = env('SECRET_KEY')
    DEBUG = env.bool('DEBUG', False)
    ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])

ROOT_URLCONF = 'project.urls'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

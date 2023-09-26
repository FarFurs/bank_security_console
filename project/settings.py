import os
# from dotenv import load_dotenv
from environs import Env


# dotenv_path = os.path.join(os.path.split(os.path.dirname(__file__))[0], '.env')
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)
env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': env.str("DB_ENGINE", default='django.db.backends.postgresql_psycopg2'),
        'HOST': env.str("DB_HOST", default='checkpoint.devman.org'),
        'PORT': env.int("DB_PORT", default=5434),
        'NAME': env.str("DB_NAME", default='checkpoint'),
        'USER': env.str("DB_USER", default=''),
        'PASSWORD': env.str("DB_PASSWORD", default=''),
    }
}


INSTALLED_APPS = ['datacenter']

SECRET_KEY = env("SECRET_KEY")

DEBUG = env.bool('DEBUG', default=False)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default='.localhost')


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

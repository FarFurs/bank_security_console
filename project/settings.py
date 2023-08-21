import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.split(os.path.dirname(__file__))[0], '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

DATABASES = {
    'default': {
        'ENGINE': os.environ["DB_ENGINE"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


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

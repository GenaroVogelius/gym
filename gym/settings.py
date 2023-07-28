



from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv() 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# !agregaste esto, .parent te permite ir un folder atrás
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
#? esto basicamente le dice que si esta en producción sea false y si esta en desarrollo sea true.
# if 'DJANGO_SETTINGS_MODULE' in os.environ:
#     # Production settings
#     DEBUG = False
# else:
#     # Development settings
#     DEBUG = True

# ? esto no creo que sea
DEBUG=True

# ! te pone siempre en False, ver para cambiar

ALLOWED_HOSTS = ["*"]
# EXTERNAL_HOSTNAME = os.environ.get('EXTERNAL_HOSTNAME')
# if EXTERNAL_HOSTNAME:    
#     ALLOWED_HOSTS.append(EXTERNAL_HOSTNAME)




INSTALLED_APPS = [
    "power_app", # !agregaste esto
    'rest_framework',# !agregaste esto
    "corsheaders",# !agregaste esto
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware", # !agregaste esto
    "django.middleware.security.SecurityMiddleware",
    # agregaste white noise
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "gym.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        #? fijate bien el path que tuviste que escribir
        "DIRS": [os.path.join(BASE_DIR, 'custom_admin/templates/'), os.path.join(BASE_DIR, 'front-end-power/dist'), os.path.join(BASE_DIR, 'power_app/templates/')], # !agregaste esto
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]




WSGI_APPLICATION = "gym.wsgi.application"




if DEBUG:
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

else:
    DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.postgresql_psycopg2",
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
    # 'default': {
    #     'ENGINE': "django.db.backends.mysql",
    #     'NAME': os.getenv('DB_NAME'),
    #     'USER': os.getenv('DB_USER'),
    #     'PASSWORD': os.getenv('DB_PASSWORD'),
    #     'HOST': os.getenv('DB_HOST'),
    #     'PORT': os.getenv('DB_PORT'),
    # }

}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "es-ar"

TIME_ZONE = "America/Argentina/Buenos_Aires"

USE_I18N = True

USE_TZ = True




#? aca le decis el path que tiene que hacer django para llegar a assets.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'front-end-power/dist/assets'), os.path.join(BASE_DIR, 'custom_admin/static')
]



# ? static url le dice a django donde buscar los archivos estaticos, como le pusiste assets va a ir a buscarlos ahi.
STATIC_URL = "/assets/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True 

if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    





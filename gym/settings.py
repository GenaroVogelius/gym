



from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv() 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# !agregaste esto, .parent te permite ir un folder atrás
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
SECRET_KEY = os.environ.get('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
# esto basicamente le dice que si esta en producción sea false y si esta en desarrollo sea true.
EXTERNAL_HOSTNAME = os.environ.get('EXTERNAL_HOSTNAME')
if EXTERNAL_HOSTNAME:
    DEBUG=False
    ALLOWED_HOSTS = []  
    ALLOWED_HOSTS.append(EXTERNAL_HOSTNAME)

else:
    DEBUG = True




INSTALLED_APPS = [
    "power_app", # !agregaste esto
    'rest_framework',# !agregaste esto
    "corsheaders",# !agregaste esto
    "django_crontab",# !agregaste esto
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
    os.path.join(BASE_DIR, 'front-end-power/dist/assets'), os.path.join(BASE_DIR, 'custom_admin/static'), os.path.join(BASE_DIR, 'power_app/static')
]



# ? static url le dice a django donde buscar los archivos estaticos, como le pusiste assets va a ir a buscarlos ahi.
STATIC_URL = "/assets/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True 
    ALLOWED_HOSTS = ["*"]

if not DEBUG:
    # !BORRAR ESTO DE ALLOWED HOSTS Y STATIC FILES
    ALLOWED_HOSTS = ["power-gym.com.ar", "www.power-gym.com.ar", "149.50.130.158"]
    ALLOWED_HOSTS.append("*")
    CORS_ALLOWED_ORIGINS = [os.environ.get('HTTPS')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
# ? This will run the delete_old_asistencias function every day at midnight (0:00). Esta libreria solo te funciona en sistema linux
CRONJOBS = [
    ('0 0 * * *', 'power_app.utils.delete_old_asistencias'), ('0 0 * * *', 'power_app.utils.delete_old_users')
]





# from pathlib import Path
# import os

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# # !agregaste esto, .parent te permite ir un folder atrás
# BASE_DIR = Path(__file__).resolve().parent.parent.parent



# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-5p46zn2l-!6^gtbxt3rirkg5y)$9b9yld^7(r5qlwc5l5$-rx-"

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False




# # Application definition

# INSTALLED_APPS = [
#     "power_app", # !agregaste esto
#     'rest_framework',# !agregaste esto
#     "corsheaders",# !agregaste esto

#     "django.contrib.admin",
#     "django.contrib.auth",
#     "django.contrib.contenttypes",
#     "django.contrib.sessions",
#     "django.contrib.messages",
#     "django.contrib.staticfiles",
# ]

# MIDDLEWARE = [
#     "corsheaders.middleware.CorsMiddleware", # !agregaste esto
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]

# ROOT_URLCONF = "gym.urls"


# TEMPLATES = [
#     {
#         "BACKEND": "django.template.backends.django.DjangoTemplates",
#         #? fijate bien el path que tuviste que escribir
#         "DIRS": [os.path.join(BASE_DIR, 'custom_admin/templates/'), os.path.join(BASE_DIR, 'front-end-power/dist')], # !agregaste esto
#         "APP_DIRS": True,
#         "OPTIONS": {
#             "context_processors": [
#                 "django.template.context_processors.debug",
#                 "django.template.context_processors.request",
#                 "django.contrib.auth.context_processors.auth",
#                 "django.contrib.messages.context_processors.messages",
#             ],
#         },
#     },
# ]




# WSGI_APPLICATION = "gym.wsgi.application"




# # ? ESTO TE LO LLEVAS A LOCAL Y PRODUCTION Y VA IR VARIANDO
# # DATABASES = {
# #     "default": {
# #         "ENGINE": "django.db.backends.sqlite3",
# #         "NAME": BASE_DIR / "db.sqlite3",
# #     }
# # }


# AUTH_PASSWORD_VALIDATORS = [
#     {
#         "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
#     },
#     {
#         "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
#     },
# ]


# LANGUAGE_CODE = "es-ar"

# TIME_ZONE = "America/Argentina/Buenos_Aires"

# USE_I18N = True

# USE_TZ = True




# # ? static url le dice a django donde buscar los archivos estaticos, como le pusiste assets va a ir a buscarlos ahi.
# STATIC_URL = "/assets/"

# #? aca le decis el path que tiene que hacer django para llegar a assets.

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'front-end-power/dist/assets'), os.path.join(BASE_DIR, 'custom_admin/static')
# ]



# DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# # esto iria en desarrollo
# # CORS_ALLOW_ALL_ORIGINS = True # !agregaste esto
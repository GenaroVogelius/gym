from .base import *


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "NAME": "railway",
#         "USER": "postgres",
#         "PASSWORD": "ZvOiAUwbh2VZAifCzwRm",
#         "HOST": "containers-us-west-28.railway.app",
#         "PORT": "6768"
#     }
# }

DATABASES = {
}

#! esto lo cambias por el host que te den en vercel
ALLOWED_HOSTS = [".vercel.app", '.now.sh', "127.0.0.1"]
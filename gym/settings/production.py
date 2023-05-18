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
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

#! esto lo cambias por el host que te den en vercel
ALLOWED_HOSTS = [".vercel.app", "localhost",
    "127.0.0.1",]
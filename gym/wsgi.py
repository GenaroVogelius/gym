"""
WSGI config for gym project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from gym.settings.base import Settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", Settings)

application = get_wsgi_application()

# !agregaste esto para vercel
app = application

"""
WSGI config for my_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.setdefault("DJANGO_ENV", "development")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_fennwords.settings." + env)

application = get_wsgi_application()

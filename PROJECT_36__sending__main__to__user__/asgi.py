"""
ASGI config for PROJECT_36__sending__main__to__user__ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PROJECT_36__sending__main__to__user__.settings')

application = get_asgi_application()

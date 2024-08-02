"""
WSGI config for stocks_products project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(key='DJANGO_SETTINGS_MODULE', value='stocks_products.settings')

application = get_wsgi_application()

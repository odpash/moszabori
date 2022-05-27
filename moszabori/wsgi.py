"""
WSGI config for moszabori project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

try:
    sys.path.remove('/usr/lib/python3/dist-packages')
except:
    pass

sys.path.append('/home/c/ca34297/public_html/moszn.ru')
sys.path.append('/home/c/ca34297/venv/lib/python3.6/site-packages')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moszabori.settings')

application = get_wsgi_application()

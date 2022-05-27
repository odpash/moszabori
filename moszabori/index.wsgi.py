import os

import sys

sys.path.append('/home/c/ca34297/public_html/moszabori')

sys.path.append('/home/c/ca34297/venv/lib/python3.6/site-packages')

os.environ['DJANGO_SETTINGS_MODULE'] = 'moszabori.settings'

import django

django.setup()

from django.core.handlers import wsgi

application = wsgi.WSGIHandler()
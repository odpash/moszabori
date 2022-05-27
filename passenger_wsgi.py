# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1257636/data/www/moszn.ru/moszabori')
sys.path.insert(1, '/var/www/u1257636/data/mz/lib/python3.9/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'moszabori.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
import os, sys

path = '/Library/Webserver/Documents/Django'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
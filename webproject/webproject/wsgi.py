"""
WSGI webproject for webproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os,sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/ec2-user/DoitProgram/webproject')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webproject.settings')

application = get_wsgi_application()


"""
WSGI config for sms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""


import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/image-cap/weather/lib/python3.4/site-packages')
# Add the app's directory to the PYTHONPATH
sys.path.append('/home/image-cap/weather-forecast')
sys.path.append('/home/image-cap/weather-forecast/sms')



from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sms.settings")

application = get_wsgi_application()
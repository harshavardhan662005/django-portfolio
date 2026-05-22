import os

from django.core.wsgi import get_wsgi_application

# Set the default settings module for the 'django' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# 1. First, create the standard Django application object
application = get_wsgi_application()

# 2. Second, point Vercel's 'app' variable directly to it
app = application
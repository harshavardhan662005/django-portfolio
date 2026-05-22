import os
import dj_database_url
from pathlib import Path

# 1. Define BASE_DIR at the top of the file before using it!
BASE_DIR = Path(__file__).resolve().parent.parent

# ... (rest of your settings like SECRET_KEY, DEBUG, ALLOWED_HOSTS)

# 2. Now this will work perfectly without errors:
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-local-development-fallback-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Allow local hosting and your future Vercel domain name
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '.vercel.app']

# Database Routing
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_local_db_name',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# If Vercel provides a cloud database URL, seamlessly switch to it in production
if os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# Static files (Vercel automatically distributes these via its CDN)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
WSGI_APPLICATION = 'config.wsgi.application'
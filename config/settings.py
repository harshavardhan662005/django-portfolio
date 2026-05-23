import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# 1. URL to use when referring to static files
STATIC_URL = '/static/'

# 2. This is where production static files will be collected (Crucial for Vercel)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# 3. Strip out STATICFILES_DIRS completely for now to see if it fixes the build
STATICFILES_DIRS = []
# Security settings
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-local-development-fallback-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Allow local hosting and your future Vercel domain name
ALLOWED_HOSTS = ['.vercel.app', 'localhost', '127.0.0.1']

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
# Absolute path to the directory where collectstatic will collect static files for deployment.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Additional locations the staticfiles app will look for static files.
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
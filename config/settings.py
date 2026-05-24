import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# Security Key - Fallback placeholder prevents crashing during Vercel's build
SECRET_KEY = os.environ.get('SECRET_KEY', 'vercel-build-placeholder-secret-key')

# Security - Keep true for debugging until it successfully loads
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.vercel.app']

# --- DATABASE SETTINGS ---
# Fallback to an in-memory SQLite database if dj_database_url can't find a live database string during build
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{os.path.join(BASE_DIR, 'db.sqlite3')}",
        conn_max_age=600
    )
}

# --- STATIC FILES SETTINGS ---
STATIC_URL = '/static/'

# Vercel needs this exact absolute path destination
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Keep this entirely empty to prevent folder-not-found build issues
STATICFILES_DIRS = []
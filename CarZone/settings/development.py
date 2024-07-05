from .base import *

# Development-specific settings
DEBUG = True

# Add 'localhost' to ALLOWED_HOSTS for development
ALLOWED_HOSTS = ['localhost', '.vercel.app', 'snipher.pythonanywhere.com']
DOMAINS = ['localhost', 'snipher.pythonanywhere.com']
SECURE_SSL_REDIRECT = False
CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://snipher.pythonanywhere.com"]

# Use SQLite for development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static and media files settings for development
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# Use console email backend for development
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
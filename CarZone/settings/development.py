from .base import *

# Development-specific settings
DEBUG = True

# Add 'localhost' to ALLOWED_HOSTS for development
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

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
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

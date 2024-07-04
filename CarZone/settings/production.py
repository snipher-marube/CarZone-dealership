from .base import *
from decouple import config, Csv
import dj_database_url

# Production-specific settings
DEBUG = True

# Add your production domain to ALLOWED_HOSTS
ALLOWED_HOSTS = ['.vercel.app']

# Configure your production database (example using PostgreSQL)
DATABASES = {
    'default': dj_database_url.config(
        default=config('POSTGRES_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# This configuration block is setting up a cache using Redis for the Django project in a production environment.
# The cache is used to store the results of expensive database queries, API calls, or other computationally expensive operations.
'''CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': config('UPSTASH_REDIS_REST_URL'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}'''

# Static and media files settings for production
STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# Use proper email backend for production (e.g., SMTP)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')

# Cloudinary storage for production
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_PRELOAD = True

DOMAIN = "https://car-zone-dealership.vercel.app"
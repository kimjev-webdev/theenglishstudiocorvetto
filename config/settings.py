from pathlib import Path
import os
import logging

# Load environment variables from the .env file
from dotenv import load_dotenv
load_dotenv()

# Import dj_database_url if you're using it
try:
    import dj_database_url
except ImportError:
    dj_database_url = None

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Read API key and other configurations from environment variables
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')

DEBUG = os.getenv("DEBUG", "False") == "True"

# Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG' if DEBUG else 'WARNING',
    },
}

# Security settings
ALLOWED_HOSTS = [
    'theenglishstudiocorvetto.onrender.com',
    'localhost',
    '127.0.0.1',
    'theenglishstudiocorvetto.com',
    'www.theenglishstudiocorvetto.com',
]

# Installed apps configuration
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'contact',
    'blog',
    'schedule',
    'cloudinary',
    'cloudinary_storage',
    'ckeditor',
    'portal',
    'flyers',
]

LOGIN_REDIRECT_URL = 'portal:portal_dashboard'
LOGIN_URL = '/portal/login/'
LOGOUT_REDIRECT_URL = 'portal:portal_login'

# Middleware configuration
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# Template settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'config.context_processors.google_maps_api_key',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database settings (using PostgreSQL or Render DB)
if os.getenv('RENDER'):
    DATABASES = {
        'default': dj_database_url.config(default='your-render-db-url')
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST', 'localhost'),
            'PORT': os.getenv('DB_PORT', '5432'),
        }
    }

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
        )
    },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
        )
    },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
        )
    },
]

# Internationalization settings
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
LANGUAGES = [('en', 'English'), ('it', 'Italian')]
LOCALE_PATHS = [BASE_DIR / 'locale']
LANGUAGE_COOKIE_NAME = 'django_language'

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "main" / "static"]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings for sending email via Gmail SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # More secure
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL')

# Blog media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Cloudinary settings for file storage
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.getenv('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.getenv('CLOUDINARY_API_KEY'),
    'API_SECRET': os.getenv('CLOUDINARY_API_SECRET'),
}

# CKEditor settings for rich text editor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Format', 'Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList'],
            ['Blockquote'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source'],
        ],
        'format_tags': 'p;h2;h3;h4;pre',
        'height': 300,
        'width': 'auto',
    }
}

# CSRF trusted origins for security
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")

# Enable logging
logger = logging.getLogger(__name__)

# Settings for auto-appending slashes in URLs
APPEND_SLASH = True

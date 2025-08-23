from pathlib import Path
import os
import logging

# .env loader (local dev)
from dotenv import load_dotenv
load_dotenv()

# Optional: dj_database_url for Render/managed DBs
try:
    import dj_database_url
except ImportError:
    dj_database_url = None

# ──────────────────────────────────────────────────────────────────────────────
# Core
# ──────────────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

DEBUG = os.getenv("DEBUG", "false").strip().lower() == "true"

# Domains
DEFAULT_ALLOWED = [
    "theenglishstudiocorvetto.onrender.com",
    "theenglishstudiocorvetto.com",
    "www.theenglishstudiocorvetto.com",
    "localhost",
    "127.0.0.1",
]
ALLOWED_HOSTS = (
    list({
        *DEFAULT_ALLOWED,
        *os.getenv("ALLOWED_HOSTS", "").split(","),
    })
    if os.getenv("ALLOWED_HOSTS")
    else DEFAULT_ALLOWED
)

# Trust Render’s proxy so reset links are HTTPS and hostnames are correct
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# CSRF trusted origins
DEFAULT_TRUSTED = [
    "https://theenglishstudiocorvetto.com",
    "https://*.onrender.com",
]
ENV_TRUSTED = [
    x
    for x in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if x
]
CSRF_TRUSTED_ORIGINS = list({*DEFAULT_TRUSTED, *ENV_TRUSTED})

# ──────────────────────────────────────────────────────────────────────────────
# 3rd-party / project config
# ──────────────────────────────────────────────────────────────────────────────
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY", "")

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "main",
    "contact",
    "blog",
    "schedule",
    "cloudinary",
    "cloudinary_storage",
    "ckeditor",
    "portal.apps.PortalConfig",  # loads signals via AppConfig
    "flyers",
]

LOGIN_REDIRECT_URL = "portal:portal_dashboard"
LOGIN_URL = "/portal/login/"
LOGOUT_REDIRECT_URL = "portal:portal_login"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # before sessions for static
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "config.context_processors.google_maps_api_key",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# ──────────────────────────────────────────────────────────────────────────────
# Database
# ──────────────────────────────────────────────────────────────────────────────
if os.getenv("RENDER") and dj_database_url:
    # Render sets DATABASE_URL – use it if present
    DATABASES = {"default": dj_database_url.config(conn_max_age=600)}
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.getenv("DB_NAME"),
            "USER": os.getenv("DB_USER"),
            "PASSWORD": os.getenv("DB_PASSWORD"),
            "HOST": os.getenv("DB_HOST", "localhost"),
            "PORT": os.getenv("DB_PORT", "5432"),
        }
    }

# ──────────────────────────────────────────────────────────────────────────────
# Passwords / Auth
# ──────────────────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        )
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        )
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        )
    },
]

# ──────────────────────────────────────────────────────────────────────────────
# I18N
# ──────────────────────────────────────────────────────────────────────────────
LANGUAGE_CODE = "en"
LANGUAGES = [("en", "English"), ("it", "Italian")]
LOCALE_PATHS = [BASE_DIR / "locale"]
LANGUAGE_COOKIE_NAME = "django_language"

TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ──────────────────────────────────────────────────────────────────────────────
# Static / Media
# ──────────────────────────────────────────────────────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "main" / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Cloudinary for user-uploaded media (static still via WhiteNoise)
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}

# ──────────────────────────────────────────────────────────────────────────────
# Email (Gmail App Password in prod, console in dev)
# ──────────────────────────────────────────────────────────────────────────────
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND",
    "django.core.mail.backends.console.EmailBackend" if DEBUG
    else "django.core.mail.backends.smtp.EmailBackend"
)

# SMTP values are used when EMAIL_BACKEND is SMTP (Render/prod)
EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", "587"))
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv(
    "EMAIL_HOST_PASSWORD", ""
)  # Gmail App Password
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "true").strip().lower() == "true"
EMAIL_USE_SSL = os.getenv("EMAIL_USE_SSL", "false").strip().lower() == "true"
EMAIL_TIMEOUT = int(os.getenv("EMAIL_TIMEOUT", "20"))

DEFAULT_FROM_EMAIL = os.getenv(
    "DEFAULT_FROM_EMAIL",
    EMAIL_HOST_USER or "noreply@theenglishstudiocorvetto.com"
)
SERVER_EMAIL = os.getenv("SERVER_EMAIL", DEFAULT_FROM_EMAIL)

# ──────────────────────────────────────────────────────────────────────────────
# CKEditor
# ──────────────────────────────────────────────────────────────────────────────
CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "Custom",
        "toolbar_Custom": [
            ["Format", "Bold", "Italic", "Underline"],
            ["NumberedList", "BulletedList"],
            ["Blockquote"],
            ["Link", "Unlink"],
            ["RemoveFormat", "Source"],
        ],
        "format_tags": "p;h2;h3;h4;pre",
        "height": 300,
        "width": "auto",
    }
}

# ──────────────────────────────────────────────────────────────────────────────
# Portal owner (env-driven)
# ──────────────────────────────────────────────────────────────────────────────
PORTAL_OWNER_USERNAME = (
    os.environ.get("PORTAL_OWNER_USERNAME", "")
    .strip()
    .lower()
)
PORTAL_OWNER_EMAIL = os.environ.get("PORTAL_OWNER_EMAIL", "").strip().lower()

# ──────────────────────────────────────────────────────────────────────────────
# Security / Misc
# ──────────────────────────────────────────────────────────────────────────────
APPEND_SLASH = True

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {
        "handlers": ["console"],
        "level": "DEBUG" if DEBUG else "WARNING",
    },
    # Optional: uncomment for more mail debugging
    # "loggers": {
    #     "django.core.mail": {"handlers": ["console"], "level": "INFO"},
    #     "smtplib": {"handlers": ["console"], "level": "INFO"},
    # },
}
logger = logging.getLogger(__name__)

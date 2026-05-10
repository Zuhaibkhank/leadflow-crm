from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# -------------------------------------------------------------------
# SECURITY SETTINGS
# -------------------------------------------------------------------

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-secret-key")

DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "leadflow-crm-5z22.onrender.com",
]


# -------------------------------------------------------------------
# INSTALLED APPS
# -------------------------------------------------------------------

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',

    # Local apps
    'accounts',
    'dashboard',
    'leads',
    'api',
]


# -------------------------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# -------------------------------------------------------------------
# ROOT URL CONFIGURATION
# -------------------------------------------------------------------

ROOT_URLCONF = 'config.urls'


# -------------------------------------------------------------------
# TEMPLATES CONFIGURATION
# -------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        # Global templates folder
        'DIRS': [BASE_DIR / 'templates'],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# -------------------------------------------------------------------
# WSGI APPLICATION
# -------------------------------------------------------------------

WSGI_APPLICATION = 'config.wsgi.application'


# -------------------------------------------------------------------
# DATABASE CONFIGURATION (PostgreSQL)
# -------------------------------------------------------------------

import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(
        os.getenv("DATABASE_URL")
    )
}


# -------------------------------------------------------------------
# PASSWORD VALIDATION
# -------------------------------------------------------------------

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# -------------------------------------------------------------------
# LANGUAGE & TIMEZONE
# -------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# -------------------------------------------------------------------
# STATIC FILES
# -------------------------------------------------------------------

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


# -------------------------------------------------------------------
# MEDIA FILES
# -------------------------------------------------------------------

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# -------------------------------------------------------------------
# LOGIN / LOGOUT REDIRECTS
# -------------------------------------------------------------------

LOGIN_URL = "login"

LOGIN_REDIRECT_URL = "dashboard:home"

LOGOUT_REDIRECT_URL = "login"


# -------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# -------------------------------------------------------------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
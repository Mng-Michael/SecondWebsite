"""
Django settings for SRCweb project.

Generated by 'django-admin startproject' using Django 3.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import platform


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('BASE_KEY')

# SECURITY WARNING: keep the AES key used in production secret!
CLEAN_AES_KEY = os.environ.get('CLEAN_AES_KEY')

# SECURITY WARNING: keep the AES key used in production secret!
NEW_AES_KEY = os.environ.get('NEW_AES_KEY')

# Discord Client ID
DISCORD_CLIENT_ID = "825618483957071873"

# SECURITY WARNING: keep the Discord Client Secret used in production secret!
DISCORD_CLIENT_SECRET = os.environ.get('DISCORD_CLIENT_SECRET')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Sends an email to admins when debug = false and a 500 server error occurs
ADMINS = [('Nick', 'nick@secondrobotics.org'), ('Brennan', 'brennan@secondrobotics.org')]

ALLOWED_HOSTS = ["secondrobotics.org", "www.secondrobotics.org"]

AUTHENTICATION_BACKENDS = [
    # 'django.contrib.auth.backends.ModelBackend', # default backend
    'discordoauth2.auth.DiscordAuthenticationBackend' # discord oauth2 backend
]

AUTH_USER_MODEL = 'discordoauth2.User'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # External packages

    'widget_tweaks',
    'rest_framework',
    'rest_framework.authtoken',

    # Custom stuff
    
    'home',
    'highscores',
    'events',
    'teamleague',
    'discordoauth2'
]

# config/settings.py
DEFAULT_FROM_EMAIL = 'noreply@secondrobotics.org'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("SMTP_SERVER")
EMAIL_HOST_USER = 'noreply@secondrobotics.org'
EMAIL_HOST_PASSWORD = os.environ.get('SMTP_PASSWORD')
EMAIL_PORT = 465
EMAIL_USE_SSL = True

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'SRCweb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'SRCweb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/images/'


plt = platform.system()
if plt == "Windows":
    DEBUG = True
    ALLOWED_HOSTS = ["localhost"]
    MEDIA_ROOT = os.path.join(BASE_DIR, "/static/media")
    STATIC_ROOT = ""
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
    DISCORD_REDIRECT_URI = "http://localhost:8000/oauth2/login/redirect"
    DISCORD_AUTH_URL = "https://discord.com/api/oauth2/authorize?client_id=825618483957071873&redirect_uri=http%3A%2F%2Flocalhost%3A8000%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify%20email"
    
else:
    STATIC_ROOT = "/home/bottxleg/secondrobotics.org/static"
    MEDIA_ROOT = "/home/bottxleg/secondrobotics.org/media"
    DISCORD_REDIRECT_URI = "https://secondrobotics.org/oauth2/login/redirect"
    DISCORD_AUTH_URL = "https://discord.com/api/oauth2/authorize?client_id=825618483957071873&redirect_uri=https%3A%2F%2Fsecondrobotics.org%2Foauth2%2Flogin%2Fredirect&response_type=code&scope=identify%20email"
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True


MAX_UPLOAD_SIZE = "5242880"

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework.renderers.JSONRenderer',
    # ),
    # 'DEFAULT_PARSER_CLASSES': (
    #     'rest_framework.parsers.JSONParser',
    # )
}
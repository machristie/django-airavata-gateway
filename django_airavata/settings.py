"""
Django settings for django_airavata_gateway project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'bots0)m91u_i4gpw+103o%2jn#j57wjh7s@9$x*27_4^*jyku4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_airavata_auth',
    'django_airavata_workspace',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_airavata_auth.middleware.authz_token_middleware',
    'django_airavata_gateway.middleware.airavata_client',
]

ROOT_URLCONF = 'django_airavata_gateway.urls'

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

WSGI_APPLICATION = 'django_airavata_gateway.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

AUTHENTICATION_BACKENDS = [
    'django_airavata_auth.backends.WSO2ISBackend'
]

WSO2IS_CLIENT_ID = 'fGwm3EW0EmaiV0jI6GBmmOiQ2Xca'
WSO2IS_CLIENT_SECRET = 'fMLLvWH6YEHwgl4Nb0hHu9AC5Jwa'
WSO2IS_AUTHORIZE_URL = 'https://localhost:9443/oauth2/authorize'
WSO2IS_TOKEN_URL = 'https://localhost:9443/oauth2/token'
WSO2IS_USERINFO_URL = 'https://localhost:9443/oauth2/userinfo?schema=openid'
WSO2IS_VERIFY_SSL = False

LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/'

GATEWAY_ID = 'php_reference_gateway'
AIRAVATA_API_HOST = 'localhost'
AIRAVATA_API_PORT = 8930
AIRAVATA_API_SECURE = False

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django_airavata_auth': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO'
        },
        'django_airavata_gateway': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO'
        },
        'django_airavata_workspace': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO'
        },
    },
}






""" Django settings for blogger project.

enerated by 'django-admin startproject' using Django 1.9.6.

For more information on this file, see 
https://docs.djangoproject.com/en/1.9/topics/settings/ For the full list 
of settings and their values, see 
https://docs.djangoproject.com/en/1.9/ref/settings/ """


import dj_database_url
import os
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n@&5n1!gx=!xqa2fmss$cc+2szp55c@*sc+tcne*yj2u)8rlr!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['45.55.128.224']


# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'blogger.apps.users',
	'blogger.apps.principal',
	'blogger.apps.principal.templatetags',
	'blogger.apps.entradas',
	'blogger.apps.multimedia',
	'mail_templated',
	'djcelery',
	'kombu.transport.django',
]

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogger.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'), ],
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

WSGI_APPLICATION = 'blogger.wsgi.application'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "pblogger42@gmail.com"
EMAIL_HOST_PASSWORD = 'xuugkqkorkkirxrm'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
	DATABASES = {}
	DATABASES['default'] = dj_database_url.config()
else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.postgresql_psycopg2',
			'NAME': 'acaima_db',
			'USER': 'acaima_db',
			'PASSWORD': 'acaima_db',
			'HOST': 'localhost',
			'PORT': '',
		}
	}
	"""
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': 'dbsqlite',
		}
	}
	"""

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/usuario/ingreso/'

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_ROOT = 'static'

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'blogger/static')

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, 'blogger/static'),
)

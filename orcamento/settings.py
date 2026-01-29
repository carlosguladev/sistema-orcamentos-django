import os
from pathlib import Path
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "0") == "1"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

RAILWAY_DOMAIN = os.environ.get("RAILWAY_PUBLIC_DOMAIN")
if RAILWAY_DOMAIN:
    ALLOWED_HOSTS.append(RAILWAY_DOMAIN)

EXTRA_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "")
if EXTRA_HOSTS:
    ALLOWED_HOSTS += [h.strip() for h in EXTRA_HOSTS.split(",") if h.strip()]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crm',
    'catalog',
    'quotes',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware'
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CSRF_TRUSTED_ORIGINS = []

if RAILWAY_DOMAIN:
    CSRF_TRUSTED_ORIGINS.append(f"https://{RAILWAY_DOMAIN}")


ROOT_URLCONF = 'orcamento.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'orcamento.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("DATABASE_URL", "sqlite:///db.sqlite3"),
        conn_max_age=600,
        ssl_require=True
    )
}



# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True
USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# Textos do admin em português simples
ADMIN_SITE_HEADER = "Sistema de Orçamentos"
ADMIN_SITE_TITLE = "Administração"
ADMIN_INDEX_TITLE = "Painel do Sistema"

JAZZMIN_SETTINGS = {

    "site_title": "Administração",
    "site_header": "Sistema de Orçamentos",
    "site_brand": "Orçamento Fácil",
    "welcome_sign": "Bem-vindo!",
    "show_sidebar": True,
    "navigation_expanded": True,

    "hide_models": ["auth.group"],  # <- some "Groups"

    "icons": {
    "auth.user": "fas fa-user",
    "auth.group": "fas fa-users",
    "crm.customer": "fas fa-user-tag",
    "catalog.catalogitem": "fas fa-box",
    "quotes.quote": "fas fa-file-invoice-dollar",
    "quotes.quoteline": "fas fa-list",
},

    "hide_models": ["auth.group"],

    "order_with_respect_to": ["quotes", "crm", "catalog", "auth"],
    
    "topmenu_links": [
    {"name": "Início", "url": "admin:index", "permissions": ["auth.view_user"]},
    {"name": "Novo Cliente", "url": "/admin/crm/customer/add/"},
    {"name": "Novo Item", "url": "/admin/catalog/catalogitem/add/"},
    {"name": "Novo Orçamento", "url": "/admin/quotes/quote/add/"},
],



}



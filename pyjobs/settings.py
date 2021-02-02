"""
Django settings for pyjobs project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

import dj_database_url
from decouple import config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = ["*"]

# E-mail
DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="pyjobs@pyjobs.com.br")

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django.contrib.sites",
    "django_extensions",
    "pyjobs.core",
    "pyjobs.api",
    "pyjobs.partners",
    "pyjobs.marketing",
    "pyjobs.synchronizer",
    "widget_tweaks",
    "django_select2",
    "django.contrib.sitemaps",
    "raven.contrib.django.raven_compat",
    "webpush",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]


ROOT_URLCONF = "pyjobs.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "pyjobs.core.context_processors.global_vars",
            ]
        },
    },
]

WSGI_APPLICATION = "pyjobs.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default="sqlite:///%s/db.sqlite3" % (BASE_DIR))
}


THUMBNAILS_BASE_FOLDER = "%s/pyjobs/core/thumb/" % (BASE_DIR)

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "pt"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_L10N = True

USE_TZ = False

LOCALE_PATHS = [os.path.join(PROJECT_ROOT, "translations")]

LANGUAGES = [
    ("pt", _("Portuguese")),
    ("en", _("English")),
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "staticfiles"),)

RAVEN_CONFIG = {"dsn": config("SENTRY_DSN", default=None)}

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "/login"

EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

SENDGRID_API_KEY = config("SENDGRID_API_KEY", default=None)

GA_CODE = config("GA_CODE", default="")

# MailChimp

MAILCHIMP_API_KEY = config("MAILCHIMP_API_KEY", default=None)
MAILCHIMP_USERNAME = config("MAILCHIMP_USERNAME", default=None)
MAILCHIMP_LIST_KEY = config("MAILCHIMP_LIST_KEY", default=None)


# Telegram

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN", default=None)
TELEGRAM_CHATID = config("TELEGRAM_CHATID", default=None)


# Recaptcha

RECAPTCHA_SECRET_KEY = config("RECAPTCHA_SECRET_KEY", default=None)

# Force SSL

if "DYNO" in os.environ:  # pragma: no cover
    SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False)
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

WEBSITE_NAME = config("WEBSITE_NAME", default=None)
WEBSITE_SLOGAN = config("WEBSITE_SLOGAN", default=None)
WEBSITE_URL = config("WEBSITE_URL", default=None)
WEBSITE_OWNER_EMAIL = config("WEBSITE_OWNER_EMAIL", default=None)
WEBSITE_OWNER_CELLPHONE = config("WEBSITE_OWNER_CELLPHONE", default=None)
WEBSITE_GENERAL_EMAIL = config("WEBSITE_GENERAL_EMAIL", default=None)
WEBSITE_WORKING_LANGUAGE = config("WEBSITE_WORKING_LANGUAGE", default=None)
WEBSITE_MAILINGLIST_LINK = config("WEBSITE_MAILINGLIST_LINK", default=None)
WEBSITE_OWNER_NAME = config("WEBSITE_OWNER_NAME", default=None)
USER_SUBSTANTIVE = config("USER_SUBSTANTIVE", default=None)
WEBSITE_HOME_URL = config("WEBSITE_HOME_URL", default=None)
MAILERLITE_API_KEY = config("MAILERLITE_API_KEY", default=None)

GITHUB_ACCESS_TOKEN = config("GITHUB_ACCESS_TOKEN", default=None)
GITHUB_ISSUES_LABELS = config("GITHUB_ISSUES_LABELS", default=None)
GITHUB_DEFAULT_REPO = config("GITHUB_DEFAULT_REPO", default=None)
WEBSITE_MANAGERS_GITHUB_NICKNAME = config(
    "WEBSITE_MANAGERS_GITHUB_NICKNAME", default=None
)

WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": config("VAPID_PUBLIC_KEY", default=None),
    "VAPID_PRIVATE_KEY": config("VAPID_PRIVATE_KEY", default=None),
    "VAPID_ADMIN_EMAIL": config("VAPID_ADMIN_EMAIL", default=None),
}

STATE_CHOICES = [
    (0, _("Acre")),
    (1, _("Alagoas")),
    (2, _("Amapá")),
    (3, _("Amazonas")),
    (4, _("Bahia")),
    (5, _("Ceará")),
    (6, _("Distrito Federal")),
    (7, _("Espírito Santo")),
    (8, _("Goiás")),
    (9, _("Maranhão")),
    (10, _("Mato Grosso")),
    (11, _("Mato Grosso do Sul")),
    (12, _("Minas Gerais")),
    (13, _("Pará")),
    (14, _("Paraíba")),
    (15, _("Paraná")),
    (16, _("Pernambuco")),
    (17, _("Piauí")),
    (18, _("Rio de Janeiro")),
    (19, _("Rio Grande do Norte")),
    (20, _("Rio Grande do Sul")),
    (21, _("Rondônia")),
    (22, _("Roraima")),
    (23, _("Santa Catarina")),
    (24, _("São Paulo")),
    (25, _("Sergipe")),
    (26, _("Tocantins")),
    (27, _("Indeterminado")),
]

SALARY_RANGES = [
    (1, "0,00 - 1.000,00"),
    (2, "1.000,01 - 3.000,00"),
    (3, "3.000,01 - 6.000,00"),
    (4, "6.000,01 - 10.000,00"),
    (5, "10.000,01 - 13.000,00"),
    (6, "13.000,01 - 16.000,00"),
    (7, "16.000,01 - 19.000,00"),
    (8, "19.000,01 - 21.000,00"),
    (9, "21.000,01 - +"),
    (10, _("NI")),
]

JOB_LEVELS = [
    (1, _("Estágio")),
    (2, _("Junior")),
    (3, _("Pleno")),
    (4, _("Sênior")),
    (5, _("Indeterminado")),
]

CONTRACT = [
    (1, _("A combinar")),
    (2, _("CLT")),
    (3, _("PJ")),
    (4, _("Estágio")),
]

FEEDBACK_TYPE = [(1, _("Sem feedback")), (2, _("Aprovado")), (3, _("Reprovado"))]

SITE_ID = config("SITE_ID", default=1, cast=int)

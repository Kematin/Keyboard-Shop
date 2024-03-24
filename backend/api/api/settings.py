from pathlib import Path

import colorlog

from api.config import CustomJsonFormatter, config

SECRET_KEY = config.SECRET_KEY
BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = config.DEBUG
ALLOWED_HOSTS = config.ALLOWED_HOSTS

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "keyboardApi",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {
            "()": "colorlog.ColoredFormatter",
            "format": "{log_color} [ {filename} {funcName} {levelname} ] {message}",
            "log_colors": {
                "DEBUG": "bold_black",
                "INFO": "cyan",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
            "style": "{",
        },
        "file": {"()": CustomJsonFormatter},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
        "django_console": {"class": "logging.StreamHandler"},
        "root_file": {
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": f"{BASE_DIR}/logs/info.log",
        },
        "django_file": {
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": f"{BASE_DIR}/logs/django_info.log",
        },
        "celery_file": {
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": f"{BASE_DIR}/logs/celery_info.log",
        },
    },
    "loggers": {
        "main": {
            "handlers": ["console"] if DEBUG else ["console", "root_file"],
            "level": "DEBUG" if DEBUG else "INFO",
        },
        "celery": {
            "handlers": ["console", "celery_file"],
            "level": "DEBUG" if DEBUG else "INFO",
        },
        "django": {"handlers": ["django_file", "django_console"], "level": "INFO"},
    },
}

ROOT_URLCONF = "api.urls"

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
            ],
        },
    },
]

WSGI_APPLICATION = "api.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

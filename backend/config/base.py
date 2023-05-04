import os
from pathlib import Path

from decouple import config
from django.utils.translation import gettext_lazy as _

#!Your everywhere service name
SITE_NAME = ""  # Domain Name


#!Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


#!App Name
APP_NAME = "TRANSACTION"  # Default ADMIN,ACCOUNT_PROFILE,TRANSACTION


#!SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY")


#!# PROD, LOCAL, DEV
ENVIRONMENT = config("ENVIRONMENT", default="LOCAL")
ALLOWED_HOSTS = (
    []
)  # In order to allow access to the Django app from any server or IP address,ensure ALLOWED_HOSTS in settings.py file set to *,as shown in the left


if ENVIRONMENT != "LOCAL":
    pass
else:
    ALLOWED_HOSTS.append("*")


#!Application definition
DEFAULT_APPS = [
    "jet.dashboard",
    "jet",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

#!Third Part App
THIRD_PARTY_APPS = [
    "rest_framework",
    "django_cleanup",
    "django_filters",
    "rest_framework.authtoken",
    "djoser",
    "corsheaders",
    "drf_spectacular",
]

#!Created Apps
CREATED_APPS = [
    "abstract",
    "account",
    "api.account_profile",
    "api.pickuplines",
    "api.transaction",
]

#!Installed Apps
INSTALLED_APPS = DEFAULT_APPS + CREATED_APPS + THIRD_PARTY_APPS


#!AUTH_USER_MODEL
AUTH_USER_MODEL = "account.Account"


#!Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


#!CORS_ALLOWED_ORIGINS
CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:5173",
    "http://localhost:3000",
    "http://localhost:5000",
    "http://localhost:9000",
]


#!CORS_ALLOW_HEADERS
CORS_ALLOW_HEADERS = [
    "app-token",
    "token",
    "accept-language",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]


#!CORS_ALLOW_CREDENTIALS
CORS_ALLOW_CREDENTIALS = True


#!CORS_ALLOW_METHODS
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]


#!Root UrlConf
ROOT_URLCONF = "config.urls"

#!Templates
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

#!Wsgi Application
WSGI_APPLICATION = "config.wsgi.application"


#!Auth Password Validators
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

#!Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/
LANGUAGE_CODE = "en"  # production => az

LANGUAGES = [
    ("az", _("Azerbaijani")),
    ("en", _("English")),
    ("ru", _("Russian")),
]
TIME_ZONE = "Asia/Baku"
# A boolean that specifies whether Django's translation system should be enabled
USE_I18N = True
# USE_L10N = True #Numbers and dates using the format of the current locale.
USE_TZ = True


#!DATE_INPUT_FORMATS
# DATE_INPUT_FORMATS = ['%m-%d-%Y']


#!Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "static/"


#!Default Auto Field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


#!Static Files
# ENVIRONMENT = config('ENVIRONMENT')
# if ENVIRONMENT == 'LOCAL':
#     STATICFILES_DIRS = [os.path.join(BASE_DIR,'static')]
# else:#if site deployed to production
#     STATIC_ROOT = os.path.join(BASE_DIR,'static')#for production

#!MediuUrl and MediaRoot
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


#!Ckeditor Upload Path
# CKEDITOR_UPLOAD_PATH = 'uploads/'


#!Jet Themes
JET_THEMES = [
    {
        "theme": "default",  # theme folder name
        "color": "#47bac1",  # color of the theme's button in user menu
        "title": "Default",  # theme title
    },
    {"theme": "violet", "color": "#a464c4", "title": "Violet"},
    {"theme": "green", "color": "#44b78b", "title": "Green"},
    {"theme": "light-green", "color": "#2faa60", "title": "Light Green"},
    {"theme": "light-violet", "color": "#a464c4", "title": "Light Violet"},
    {"theme": "light-blue", "color": "#5EADDE", "title": "Light Blue"},
    {"theme": "light-gray", "color": "#222", "title": "Light Gray"},
]


#!Rest Framework
REST_FRAMEWORK = {
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


#!SPECTACULAR_SETTINGS
SPECTACULAR_SETTINGS = {
    "TITLE": "Django Rest Api PickupLines Project",
    "DESCRIPTION": "This project purpose creating web3 api for custom purpose",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

#!Scheme Docs Url EndPoint => http://127.0.0.1:8000/api/schema/docs

# Python Modules and Functions
import sys

# Create custom path for impor other models file from another path,if you not define this django not found app and
sys.path.append("..")


from ..base import *
from decouple import config

#!Debug
DEBUG = True


#!Databases

# Default Sqlite For Development
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Migrate Postgress and Docker
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql_psycopg2",
#         "HOST": config("POSTGRES_HOST"),
#         "NAME": config("POSTGRES_DB"),
#         "USER": config("POSTGRES_USER"),
#         "PASSWORD": config("POSTGRES_PASSWORD"),
#         "PORT": config("POSTGRES_PORT", 5432),
#         "DISABLE_SERVER_SIDE_CURSORS": True,
#     }
# }

#!Installed Apps
INSTALLED_APPS += []


#!Middleware
MIDDLEWARE += []

"""
    These commented config will use when you are runnning the project on Docker
"""

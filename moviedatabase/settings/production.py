import os
from .base import *
import dj_database_url


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-p)ucdafyxxh@g$f9mywzv$qssx20^70)8sgol*1v339eqi@^4%'
SECRET_KEY = os.environ["SECRET_KEY"]
# SECURITY W`ARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get("DATABASE_URL"))

DATABASES = {"default": DEFAULT_CONNECTION}
import os
from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-p)ucdafyxxh@g$f9mywzv$qssx20^70)8sgol*1v339eqi@^4%'
SECRET_KEY = os.environ["SECRET_KEY"]
# SECURITY W`ARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

ALLOWED_HOSTS = ['0.0.0.0', 'localhost']

    
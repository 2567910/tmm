import os

from .base import *


DEBUG = False
USE_DEBUG_TOOLBAR = False
LATEX_SILENT = True

DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('PRODUCTION_SECRET_KEY')

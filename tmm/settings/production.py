import os

from .base import *


DEBUG = False
USE_DEBUG_TOOLBAR = False
LATEX_SILENT = True

DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y1j)cbl^idh4-t%yo2)o84nd0l)v=n&%v=v^kr$ka77)a-uja*'

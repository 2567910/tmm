import os

from .base import *

DEBUG = False
USE_DEBUG_TOOLBAR = False

ALLOWED_HOSTS = ['tmm.azure.blu-beyond.com'] # Sets the url where the application is available

# Force SSL
DATABASES['default']['OPTIONS'] = {'sslmode': 'require'}

SECRET_KEY = 'y1j)cbl^idh4-t%yo2)o84nd0l)v=n&%v=v^kr$ka77)a-uj12'

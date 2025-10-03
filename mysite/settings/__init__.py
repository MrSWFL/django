# django/mysite/config/settings/__init__.py

# Setting Environment Variables:
#   In production, set the DJANGO_ENV environment variable to 'production':
#     export DJANGO_ENV=production

import os

env = os.environ.get('DJANGO_ENV', 'local')

if env == 'production':
    from .production import *
else:
    from .local import *

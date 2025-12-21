import os
from django.core.wsgi import get_wsgi_application

# Make sure this matches your project module folder
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telcoriskiq.settings')

application = get_wsgi_application()

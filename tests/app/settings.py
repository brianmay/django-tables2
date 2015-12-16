import six
from django.conf import global_settings

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'tests.app',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django_tables2',
]

ROOT_URLCONF = 'tests.app.urls'

SECRET_KEY = "this is super secret"

try:
    TEMPLATE_CONTEXT_PROCESSORS = [
        'django.core.context_processors.request'
    ] + list(global_settings.TEMPLATE_CONTEXT_PROCESSORS)
except AttributeError:
    # django master doesn't define global_settings.TEMPLATE_CONTEXT_PROCESSORS
    # anymore, use the Django>=1.8 TEMPLATES setting to add the context
    # processor. Can be simplified to only TEMPLATES if we drop 1.7 support
    import os
    TEMPLATES = [{
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(os.path.abspath(__file__), 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    }]

TIME_ZONE = "Australia/Brisbane"

USE_TZ = True

if not six.PY3:  # Haystack isn't compatible with Python 3
    INSTALLED_APPS += [
        'haystack',
    ]
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        }
    }

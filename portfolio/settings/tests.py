from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "pytest",
        "USER": "pytest",
        "PASSWORD": "pytest",
        "HOST": "localhost",
        "PORT": 5433,
    },
}

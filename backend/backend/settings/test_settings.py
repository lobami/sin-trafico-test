from .dev import Dev
import os
import pytest
from django.db import connections

import psycopg2
import json


class TestCong(Dev):
    # SECRET_KEY = '&8o&4z%7$vpux^*022f%eaffc*k1-28%n)hccxyj0gty%)m*w$'
    """
    @pytest.fixture(scope='session')
    def django_db_setup():
        Dev.DATABASES['default'] = {
            'ENGINE': 'django.db.backends.sqlite3',
            'HOST': 'db.example.com',
            'NAME': 'external_db',
        }
    """
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'backend',
        },

    }


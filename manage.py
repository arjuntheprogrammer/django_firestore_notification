#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_firestore.settings'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(
        BASE_DIR,
        "django_firestore/firebase_config/****.json")
    print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

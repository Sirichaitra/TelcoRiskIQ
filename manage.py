#!/usr/bin/env python
import os
import sys

# Add project root to PYTHONPATH automatically
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telcoriskiq.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and your virtual environment is active."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

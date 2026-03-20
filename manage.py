#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import argparse


def main():
    """Run administrative tasks."""
    # Parse config-file argument if present (for compatibility with start_app.py)
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--config-file", type=str, default="")
    args, remaining = parser.parse_known_args()
    
    # Store config file path in environment variable for settings.py to use
    if args.config_file:
        os.environ["EUD_CONFIG_FILE"] = args.config_file
    
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eud_gui.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line([sys.argv[0]] + remaining)


if __name__ == '__main__':
    main()

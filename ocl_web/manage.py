"""
ocl_web manage.py
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")
    os.environ.setdefault("DJANGO_SECRET_KEY", "secret")

    from configurations.management import execute_from_command_line

    if os.environ.get('DJANGO_CONFIGURATION') in ['Staging', 'Production', 'Showcase']:
        import newrelic.agent
        newrelic.agent.initialize('/root/newrelic.ini')

    execute_from_command_line(sys.argv)

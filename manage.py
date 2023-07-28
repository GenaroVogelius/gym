"""Django's command-line utility for administrative tasks."""
import os
import sys



def main():
    # !Esto de aca le dice donde buscar las settings
    # if base.DEBUG:
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gym.settings.local")
    # else:
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gym.settings.production")

    # si el debug esta en true va a ir a las settings locales sino a las de produccion
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gym.settings")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

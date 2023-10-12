import logging


class DisableReload(logging.Filter):
    def filter(self, record):
        if record.name == "django.utils.autoreload":
            return False
        return True

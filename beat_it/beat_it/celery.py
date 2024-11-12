import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beat_it.settings")

app = Celery("beat_it")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

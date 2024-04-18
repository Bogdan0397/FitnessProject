# import os
# import time
#
# from celery import Celery
# from django.conf import settings
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','fitness_app.settings')
#
# app = Celery('fitness_app')
# app.config_from_object('django.conf:settings')
# app.conf.broker_url = settings.CELERY_BROKER_URL
# app.autodiscover_tasks()


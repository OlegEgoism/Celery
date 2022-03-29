import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'site_celery.settings')

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('site_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'

# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'main.tasks.hello_oleg',
#         'schedule': 10.0,
#         'args': ('Dima_BEST',),
#     },
# }
# app.conf.timezone = 'UTC'
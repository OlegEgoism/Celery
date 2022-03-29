import requests
from urllib.parse import urlparse
from celery import Celery
from celery.exceptions import Reject
from bs4 import BeautifulSoup

app = Celery(
    'my_celery.tasks',
    broker='redis://127.0.0.1:6379/0',
    backend='redis://127.0.0.1:6379/0',
)

app.conf.task_send_sent_event = True

@app.task(
    autoretry_for=(requests.HTTPError,),
    retry_kwargs={'max_retries': 3},
    retry_backoff=True,
    acks_late=True  # required if we want to task-rejected event to be sent
)


@app.task(track_started=True)
def fn_1(a, b):
    return a*b


@app.task(track_started=True)
def fn_2(a, b):
    c = a**b**1000
    return c


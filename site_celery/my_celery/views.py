import re
import redis
from django.conf import settings
from django.shortcuts import render
from .forms import InfoForm
from .tasks import *
import json

def index(request):
    form = InfoForm()
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['number_1']
            b = form.cleaned_data['number_2']
            fn_1.delay(a, b)
            fn_2.delay(a, b)
    context = {
        'form': form
    }
    return render(request, 'index.html', context)


def finish(request):
    redis_instance = redis.StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    items = [key.decode('utf-8') for key in redis_instance.keys('*') if
             re.match('celery-task-meta-.*', key.decode('utf-8'))]
    status = [(json.loads(redis_instance.get(value)).get("status"), json.loads(redis_instance.get(value)).get("result")) for value in items]

    # resalts = [json.loads(redis_instance.get(value)).get("status") for value in items]
    context = {
        'redis_instance_keys': status
    }
    return render(request, 'finish.html', context)



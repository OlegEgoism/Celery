from django.urls import path
from .views import index, finish


urlpatterns = [
    path('1', index),
    path('finish', finish),
]

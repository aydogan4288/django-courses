from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^(?P<number>\d+)/delete$', views.delete),
    url(r'^(?P<number>\d+)/destroy$', views.destroy),


]

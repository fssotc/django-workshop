from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^(?P<name>\w+)/$', views.index, name='index'),
        ]

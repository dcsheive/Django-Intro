from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process/$', views.process),
    url(r'^back/$', views.back),
    url(r'^clear/$', views.clear), 
    url(r'^success/$', views.success)
]
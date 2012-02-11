from django.conf.urls.defaults import *
from project.t1.views import *

urlpatterns = patterns('',
    url(r'^$', index),
)

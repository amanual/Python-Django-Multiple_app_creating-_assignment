from django.conf.urls import url
from . import views
urlpatterns = [
    # url(r'^$', views.index),
    url(r'^$', views.surveys),
    url(r'^new/$', views.new)
    
]
from django.conf.urls import url
from . import views
urlpatterns =[
    url(r'^', views.home),
    url(r'^', views.base),
    url(r'^', views.tform),
    url(r'^', views.insert),
]
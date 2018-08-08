"""mlweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url , include
from django.contrib import admin
from db1 import views
from eexam import views
from .views import home , index , form , index2 , index3 , predicpage , abc , connect , tform , insert , emailtest
from testz import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.decorators.csrf import csrf_exempt

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home),
    url(r'^index.html$', index),
    url(r'^form', form),
    url(r'^index2.html$', index2),
    url(r'^index3.html$', index3),
    url(r'^predicpage.html$', predicpage),
    url(r'^abc.html', abc),
    url(r'^connect.php$', connect),
    url(r'^eexam/login.html', include('eexam.urls')),
    url(r'^tform.html', tform),
    url(r'^insert.php', insert),
    url(r'^emailtest.html', emailtest),
    url(r'^testz/login.html', include('testz.urls')),

]

urlpatterns += staticfiles_urlpatterns()
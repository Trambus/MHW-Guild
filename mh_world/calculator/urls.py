from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mh_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.calculator, name="calculator")
]

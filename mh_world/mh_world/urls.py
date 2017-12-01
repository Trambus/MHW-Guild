from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mh_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.home, name="home"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^calculator/', include('calculator.urls')),
    url(r'^monsters/', include('monsters.urls')),
    url(r'^weapons/', include('weapons.urls')),
    url(r'^armors/', include('armors.urls')),
    url(r'^items/', include('items.urls'))
]

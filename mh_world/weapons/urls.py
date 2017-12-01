from django.conf.urls import include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mh_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Weapon category pages
    url(r'^$', views.weapons, name="weapons"),
    url(r'^1/$', views.swordShield, name="sword and shield"),
    url(r'^2/$', views.dualBlades, name="dual blades"),
    url(r'^3/$', views.longsword, name="longsword"),
    url(r'^4/$', views.lightBowgun, name="light bowgun"),
    url(r'^greatsword/$', views.greatsword, name="greatsword"),
    url(r'^hammer/$', views.hammer, name="hammer"),
    url(r'^lance/$', views.lance, name="lance"),
    url(r'^gunlance/$', views.gunlance, name="gunlance"),
    url(r'^heavy-bowgun/$', views.heavyBowgun, name="heavy bowgun"),
    url(r'^hunting-horn/$', views.huntingHorn, name="hunting horn"),
    url(r'^switch-axe/$', views.switchAxe, name="switch axe"),
    url(r'^charge-blade/$', views.chargeBlade, name="charge blade"),
    url(r'^insect-glaive/$', views.insectGlaive, name="insect glaive"),
    url(r'^bow/$', views.bow, name="bow")


    # Sword & Shields

    # Dual blades

    # Longswords

    # Light Bowguns

    # Greatswords

    # Hammers

    # Lances

    # Gunlances

    # Heavy Bowguns

    # Hunting Horns

    # Switch Axes

    # Charge blades

    # Insect Glaives

    # Bows

]

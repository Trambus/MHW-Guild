from django.shortcuts import render
from django.template import loader
from .models import weapon

# Create your views here.
def weapons(request):
    weapon_types = weapon.objects.all()
    context = {'weapon_types':weapon_types}
    return render(request, "base_weapons.html", context)

def swordShield(request):
    # context = {}
    return render(request, "weapon.html", context)

def dualBlades(request):
    # context = {}
    return render(request, "weapon.html", context)

def longsword(request):
    # context = {}
    return render(request, "weapon.html", context)

def lightBowgun(request):
    # context = {}
    return render(request, "weapon.html", context)

def greatsword(request):
    # context = {}
    return render(request, "weapon.html", context)

def hammer(request):
    # context = {}
    return render(request, "weapon.html", context)

def lance(request):
    # context = {}
    return render(request, "weapon.html", context)

def gunlance(request):
    # context = {}
    return render(request, "weapon.html", context)

def heavyBowgun(request):
    # context = {}
    return render(request, "weapon.html", context)

def huntingHorn(request):
    # context = {}
    return render(request, "weapon.html", context)

def switchAxe(request):
    # context = {}
    return render(request, "weapon.html", context)

def chargeBlade(request):
    # context = {}
    return render(request, "weapon.html", context)

def insectGlaive(request):
    # context = {}
    return render(request, "weapon.html", context)

def bow(request):
    # context = {}
    return render(request, "weapon.html", context)

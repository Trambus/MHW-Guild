from django.shortcuts import render

# Create your views here.
def armors(request):
    return render(request, "base_armors.html")

from django.shortcuts import render
from .models import City

def home(request):
    cities = City.objects.all()
    return render(request, 'home.html', {'cities': cities})
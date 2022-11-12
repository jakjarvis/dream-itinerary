from django.shortcuts import render
from django.http import HttpResponse
from .models import Trip, Activity

# Create your views here.


def home(request):
    trips = Trip.objects.all()
    return render(request, "trips/home.html", {"trips": trips})

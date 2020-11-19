from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'store/home.html')

def all_flights(request):
    return render(request, 'store/flights.html')

def all_hotels(request):
    return render(request, 'store/hotels.html')

# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flights
from django.views import View
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'store/home.html')

class AllFlights (View):
    def get (self,request):
        flights = Flights.get_all_flights().order_by('time')
        return render(request, 'store/flights.html', {'flights' : flights})
    def post (self,request):
        fromloc = request.POST.get('from')
        toloc = request.POST.get('to')
        tdate = request.POST.get('date')
        trange = request.POST.get('range')
        print(trange)
        frm_flts = Flights.objects.filter(fromdest__icontains = fromloc).order_by('time')
        to_flts = Flights.objects.filter(todest__icontains = toloc).order_by('time')
        print(to_flts)
        if (tdate != ""):
            dt_flts = Flights.objects.filter(time__range=[tdate, "2023-01-31"]).order_by('time')
        else:
            dt_flts = Flights.get_all_flights().order_by('time')
        search_flts = frm_flts & to_flts & dt_flts
        return render (request,'store/flights.html', {'flights': search_flts, 'fromloc': fromloc, 'toloc': toloc, 'tdate': tdate})

def all_hotels(request):
    return render(request, 'store/hotels.html')

# Create your views here.
def loginpage(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = 'username', password = 'password')

        if user is not None:
            login(request, user)
            redirect('index')
    
    context = {}
    return render(request, 'store/login.html', context)

def profilepage(request):
    context = {}
    return render(request, 'store/profile.html', context)
    
"""
    context = {}
    if request.method=='POST':
        return render(request, 'store/profile.html', context)

    else:
        return render(request, 'store/login.html', context)
"""
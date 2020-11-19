from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'store/home.html')

def all_flights(request):
    return render(request, 'store/flights.html')

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
    return render(request, 'accounts/login.html', context)



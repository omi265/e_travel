from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flights, Hotel, Customer, create_or_update_user_profile
#from .forms import Updateuserinfo, Updatecustomerinfo
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView

#from django.contrib.auth.decorators import login_required

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

def bookFlts(request):
    return render(request, 'store/book.html')

class AllHotels (View):
    def get (self,request):
        hotels = Hotel.get_all_hotels().order_by('name')
        return render(request, 'store/hotels.html', {'hotels' : hotels})
    def post (self,request):
        lochotel = request.POST.get('place')
        nameofhotel = request.POST.get('name')
        rating = request.POST.get('stars')
        print(lochotel)
        lochotels = Hotel.objects.filter(place__icontains = lochotel).order_by('name')
        if (rating != ""):
            disphotels = Hotel.objects.filter(stars__icontains = rating).order_by('name')
        else:
            disphotels = Hotel.get_all_hotels().order_by('name')
        search_hotels = lochotels & disphotels
        return render (request,'store/hotels.html', {'hotels': search_hotels, 'lochotel': lochotel, 'nameofhotel': nameofhotel, 'rating': rating})

def loginpage(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = 'username', password = 'password')

        if user is not None:
            login(request, user)
            return redirect('index')
    
    context = {}
    return render(request, 'store/login.html', context)

def logoutpage(request):
    logout(request)

class profilepage(UpdateView):
    def get(self , request):
        return render(request, 'store/profile.html')

    def post(self , request):
        postData=request.POST
        name=postData.get('name')
        phone=postData.get('phone')
        email=postData.get('email')
        
        value = {'name': name, 'phone': phone, 'email': email}

        customer = Customer(name=name, phone=phone, email=email)
        create_or_update_user_profile(User, Customer, created=True)
        print(name, phone, email)
        customer.register()

        return redirect('/store/')

"""
def profilepage(request):
    context = {}
    return render(request, 'store/profile.html', context)
"""
"""
@login_required 
def profilepage(request):
    userupdateform = Updateuserinfo()
    customerupdateform = Updatecustomerinfo()

    context = {'customerupdateform': customerupdateform, 'userupdateform': userupdateform}
    return render(request, 'store/profile.html', context)
"""    

    
"""
    if request.method == 'POST':
        userupdate = Updateuserinfo(request.POST, instance=request.user)
        customerupdate = Updatecustomerinfo(request.POST, request.FILES, instance=request.user.Customer)
        if userupdate.is_valid() and customerupdate.is_valid():
            userupdate.save()
            customerupdate.save()
            messages.success(request,'Update successful')
            return redirect('profile')
    else:
        userupdate = Updateuserinfo(instance=request.user)
        customerupdate = Updatecustomerinfo(instance=request.user.Customer)

    context = {'customerupdate':customerupdate, 'userupdate': userupdate}
    return render(request, 'store/profile.html', context)
    """
"""
    context = {}
    if request.method=='POST':
        return render(request, 'store/profile.html', context)

    else:
        return render(request, 'store/login.html', context)
"""
from django.shortcuts import render, redirect
from django.http import HttpResponse
<<<<<<< HEAD
from .models import Flights, Hotel, Customer, create_or_update_user_profile
#from .forms import Updateuserinfo, Updatecustomerinfo
=======
from .models import Flights, Hotel, Ticket, Customer
>>>>>>> 36aa7ca54161a0313232e1571f2e04f728d70e2a
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

class BookFlts (View):
    def get (self,request):
        flt_code = request.GET.get('flight')
        print(flt_code)
        flt_obj = Flights.objects.filter(code = flt_code)
        print(flt_obj)
        return render(request, 'store/book.html', {'flt': flt_code})

    def post (self,request):
        flt_code = request.POST.get('flight')
        print(flt_code)
        flt_obj = Flights.objects.filter(code = flt_code)
        cust_obj = Customer.objects.filter(id = 1)
        print(cust_obj)
        cust_obj = list(cust_obj)
        passengers = []
        no_pass = request.POST.get('select')
        no_pass = int(no_pass)
        price = 0
        for flt in flt_obj:
            price = flt.price * no_pass
        for i in range (0,no_pass):
            passengers.append(i+1)

        name_1 = request.POST.get('name_1')
        age_1 = request.POST.get('age_1')
        gender_1 = request.POST.get ('gender_1')
        print(gender_1)
        name_2 = request.POST.get('name_2')
        age_2 = request.POST.get('age_2')
        gender_2 = request.POST.get ('gender_2')
        name_3 = request.POST.get('name_3')
        age_3 = request.POST.get('age_3')
        gender_3 = request.POST.get ('gender_3')
        name_4 = request.POST.get('name_4')
        age_4 = request.POST.get('age_4')
        gender_4 = request.POST.get ('gender_4')
        name_5 = request.POST.get('name_5')
        age_5 = request.POST.get('age_5')
        gender_5 = request.POST.get('gender_5')
        type_flt = request.POST.get('type')

        if(name_1):
            flt_code = request.POST.get('flight')
            print(flt_code)
            flt_obj = Flights.objects.filter(code = flt_code)
            print(flt_obj)
            flt_objl = list(flt_obj)
            print(flt_obj)
            for flt in flt_objl:
                for cust in cust_obj:
                    ticket_save = Ticket(
                    flight= flt,
                    customer=cust,
                    pas1_name= name_1,
                    pas1_age = age_1,
                    pas1_gen = gender_1,
                    pas2_name= name_2,
                    pas2_age = age_2,
                    pas2_gen = gender_2,
                    pas3_name= name_3,
                    pas3_age = age_3,
                    pas3_gen = gender_3,
                    pas4_name= name_4,
                    pas4_age = age_4,
                    pas4_gen = gender_4,
                    pas5_name= name_5,
                    pas5_age = age_5,
                    pas5_gen = gender_5,
            )
                
            ticket_save.save()
            if (ticket_save):
                if (type_flt == "Economy"):
                    for flt in flt_obj:
                        num_seats = flt.ns
                        num_econ = flt.nsle
                        num_seats = num_seats - no_pass
                        num_econ = num_econ -no_pass
                        flt.ns = num_seats
                        flt.nsle = num_econ
                        flt.save()
                if (type_flt == "Business"):
                    for flt in flt_obj:
                        num_seats = flt.ns
                        num_bus = flt.nslb
                        num_seats = num_seats - no_pass
                        num_bus = num_bus -no_pass
                        flt.ns = num_seats
                        flt.nslb = num_bus
                        flt.save()
                if (type_flt == "First Class"):
                    for flt in flt_obj:
                        num_seats = flt.ns
                        num_fc = flt.nslf
                        num_seats = num_seats - no_pass
                        num_fc = num_fc -no_pass
                        flt.ns = num_seats
                        flt.nslf = num_fc
                        flt.save()
                return render(request, 'store/ticket.html', {'ticket': ticket_save, 'flight': flt_obj, 'type': type_flt, 'price': price})
            
        

        return render(request, 'store/book.html', {'passengers': passengers, 'num_pass': no_pass, 'flt': flt_code, 'price': price})

def ticket(request):
    return render(request, 'store/ticket.html')

# def bookFlts(request):
#     return render(request, 'store/book.html')

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
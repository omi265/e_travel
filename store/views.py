from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Flights, Hotel, Ticket, Customer, Rooms, Airlines, Location
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import Updatecustomerinfo, Updateuserinfo
#csv
import csv, io
from django.contrib.auth.decorators import permission_required 
from django.contrib import messages

#from .signals import create_custprofile, save_custprofile

def index(request):
    return render(request, 'store/home.html')

class AllFlights (View):
    def get (self,request):
        flights = Flights.get_all_flights().order_by('time')
        lines = Airlines.objects.all()
        return render(request, 'store/flights.html', {'flights' : flights, 'airlines': lines})
    def post (self,request):
        lines = Airlines.objects.all()
        fromloc = request.POST.get('from')
        toloc = request.POST.get('to')
        tdate = request.POST.get('date')
        print(tdate)
        if (tdate != ""):
            tdate = datetime.datetime.strptime(tdate, "%Y-%m-%d")
            date = tdate
        else:
            date = datetime.date.today()
        print(tdate)
        wifi = request.POST.get('obw')
        non_stop = request.POST.get('non_stop')
        early_morning = request.POST.get('early_morning')
        morning = request.POST.get('morning')
        afternoon = request.POST.get('afternoon')
        night = request.POST.get('night')
        search_flts = Flights.get_all_flights().order_by('time')
        airlines = request.POST.getlist('airlines[]')
        print(airlines)
        air_flts = Flights.objects.none()
        for air in airlines:
            air_name = Airlines.objects.filter(airline = air)
            for name in air_name:
                f = Flights.objects.filter(airline = name.id)
                # air_flts = (air_flts | Flights.objects.filter(airline = name.id)).distinct()
                air_flts = air_flts | f
        
        if (airlines == []):
            air_flts = Flights.get_all_flights().order_by('time')
        print(air_flts)
        if(wifi != None):
            src_flts = Flights.objects.filter(obw__icontains = "Yes").order_by('time')
        else:
            src_flts = Flights.get_all_flights().order_by('time')

        if(non_stop != None):
            non_flts = Flights.objects.filter(no_stops__icontains = 0).order_by('time')
        else:
            non_flts = Flights.get_all_flights().order_by('time')
    
        if(early_morning != None):
            strt_time  = datetime.datetime.combine(date, datetime.time(0, 00))
            end_time = datetime.datetime.combine(date, datetime.time(6, 00))
            em_flts = Flights.objects.filter(time__range=[strt_time, end_time]).order_by('time')
            
        else:
            em_flts = Flights.get_all_flights().order_by('time')

        if(morning != None):
            strt_time  = datetime.datetime.combine(date, datetime.time(6, 00))
            end_time = datetime.datetime.combine(date, datetime.time(12, 00))
            m_flts = Flights.objects.filter(time__range=[strt_time, end_time]).order_by('time')
        else:
            m_flts = Flights.get_all_flights().order_by('time')

        if(afternoon != None):
            strt_time  = datetime.datetime.combine(date, datetime.time(12, 00))
            end_time = datetime.datetime.combine(date, datetime.time(18, 00))
            a_flts = Flights.objects.filter(time__range=[strt_time, end_time]).order_by('time')
            print(a_flts)
        else:
            a_flts = Flights.get_all_flights().order_by('time')

        if(night != None):
            strt_time  = datetime.datetime.combine(date, datetime.time(18, 00))
            end_time = datetime.datetime.combine(date, datetime.time(23, 59))
            n_flts = Flights.objects.filter(time__range=[strt_time, end_time]).order_by('time')
        else:
            n_flts = Flights.get_all_flights().order_by('time')


        if (fromloc != None or toloc != None or tdate != None):
            frm_flts = Flights.objects.filter(fromdest__icontains = fromloc).order_by('time')
            to_flts = Flights.objects.filter(todest__icontains = toloc).order_by('time')
            if (tdate != ""):
                dt_flts = Flights.objects.filter(time__range=[tdate, "2023-01-31"]).order_by('time')
            else:
                dt_flts = Flights.get_all_flights().order_by('time')
            search_flts = frm_flts & to_flts & dt_flts
        else:
            fromloc = {}
            toloc = {}
        search_flts= search_flts & non_flts & src_flts & em_flts & m_flts & a_flts & n_flts & air_flts
        if (tdate != ""):
            tdate = tdate.strftime("%Y-%m-%d")
        return render (request,'store/flights.html', {'flights': search_flts, 'fromloc': fromloc, 'toloc': toloc, 'tdate': tdate, 'airlines': lines})

# class Filter (View):
#     def post (self,request):
#         wifi = request.POST.get('obw')
#         non_stop = request.POST.get('non_stop')
#         print(wifi)
#         print(non_stop)

class BookFlts (View):
    def get (self,request):
        flt_code = request.GET.get('flight')
        flt_obj = Flights.objects.filter(code = flt_code)
        price = {}
        return render(request, 'store/book.html', {'flt': flt_code, 'price': price})

    def post (self,request):
        flt_code = request.POST.get('flight')
        print(flt_code)
        flt_obj = Flights.objects.filter(code = flt_code)
        #cust_obj = Customer.objects.filter(id = 1)
        cust_obj = User.objects.filter(id = request.user.id)
        print(cust_obj)
        cust_obj = list(cust_obj)
        passengers = []
        no_pass = request.POST.get('select')
        no_pass = int(no_pass)
        price = 0
        type_flt = request.POST.get('type')
        for flt in flt_obj:
            if (type_flt == "Economy"):
                price = flt.price_e * no_pass
            if (type_flt == "Business"):
                price = flt.price_b * no_pass
            if (type_flt == "First Class"):
                price = flt.price_fc * no_pass
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
                    user=cust,
                    #customer=cust,
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
            
        

        return render(request, 'store/book.html', {'passengers': passengers, 'num_pass': no_pass, 'type': type_flt, 'flt': flt_code, 'price': price})

def history(request):
    csu_id = request.user.username #current user's id
    print(csu_id)
    cust_obj = User.objects.filter(username = csu_id)
    print(cust_obj)
    # cust_obj = Customer.objects.filter(id = 1)
    tickets = Ticket.get_by_user(cust_obj)
    return render(request, 'store/history.html', {'tickets': tickets})

# def bookFlts(request):
#     return render(request, 'store/book.html')

class AllHotels (View):
    def get (self,request):
        hotels = Hotel.get_all_hotels().order_by('name')
        places = Location.objects.all()
        print(hotels)
        return render(request, 'store/hotels.html', {'hotels' : hotels, 'location': places})

    def post (self,request):
        places = Location.objects.all()
        loc = request.POST.get('place')
        stdate = request.POST.get('date')
        print(stdate)
        if (stdate != ""):
            stdate = datetime.datetime.strptime(stdate, "%Y-%m-%d")
            date = stdate
        else:
            date = datetime.date.today()
        print(stdate)

        search_htls = Hotel.get_all_hotels().order_by('name')
        location = request.POST.getlist('location[]')
        print(location)
        air_htls = Hotel.objects.none()
        for locs in location:
            htl_name = Hotel.objects.filter(place = loc)
            for name in htl_name:
                h = Hotel.objects.filter(location = name.id)
                # air_flts = (air_flts | Flights.objects.filter(airline = name.id)).distinct()
                air_htls = air_htls | h
        if (places == []):
            air_htls = Hotel.get_all_hotels().order_by('name')
        print(air_htls)
        search_htls= search_htls & air_htls 
        if (stdate != ""):
            stdate = stdate.strftime("%Y-%m-%d")
        return render (request,'store/hotels.html', {'hotels': search_htls, 'loc': loc, 'stdate': stdate, 'places': places})

#---------------------------------------------------------------------------------------------------------------
"""
        lochotel = request.POST.get('place')
        #nameofhotel = request.POST.get('name')
        #rating = request.POST.get('stars')
        print(lochotel)
        tdate = request.POST.get('date')
        print(tdate)
        if (tdate != ""):
            tdate = datetime.datetime.strptime(tdate, "%Y-%m-%d")
            date = tdate
        else:
            date = datetime.date.today()
        print(tdate)
        l_hotels = Hotel.objects.filter(place__icontains = lochotel).order_by('name') ###########################
        #if (rating != ""):
        #    disphotels = Hotel.objects.filter(stars__icontains = rating).order_by('name')
        #else:
        #    disphotels = Hotel.get_all_hotels().order_by('name')
        #search_hotels = lochotels & disphotels
        search_hotels = l_hotels ###########################
        return render (request,'store/hotels.html', {'hotels': search_hotels, 'lochotel': lochotel, 'nameofhotel': nameofhotel, 'rating': rating})
"""
#----------------------------------------------------------------------------------------------------------------------

def loginpage(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = 'username', password = 'password')

        if user is not None:
            login(request, user)
            #csui = request.user.id #current users id
            #print(csui)
            return redirect('index')
    
    context = {}
    return render(request, 'store/login.html', context)

def logoutpage(request):
    logout(request)
"""
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
        current_user = request.user.username
        print(current_user)
        #current_user = User(first_name=name, email=email)
        #create_or_update_user_profile(User, Customer, created=True)
        print(name, phone, email)
        customer.register()

        return redirect('/store/')
"""
"""
#@login_required
def profilepage(request):
    if request.method == 'GET':
        return render(request, 'store/profile.html')

    elif request.method == 'POST':
        postData=request.POST
        name=postData.get('name')
        phone=postData.get('phone')
        email=postData.get('email')

        value = {'name': name,'phone': phone, 'email': email}
        current_user = request.user 
        customer = Customer(name=name, phone=phone, email=email)
        print(request.user.username)
        current_user.customer.name=name
        current_user.customer.phone=phone
        current_user.customer.email=email
        print(customer.name)
        customer.register()

        return render(request, 'store/profile.html')

"""

@login_required 
def profilepage(request):
    if request.method == 'POST':
        userupdate = Updateuserinfo(request.POST, instance=request.user)
        customerupdate = Updatecustomerinfo(request.POST, request.FILES, instance=request.user.customer)

        userupdate.save()
        customerupdate.save()
        messages.success(request, f'Account Information Updated!')

        return redirect('/store/profile/')

    else:
        userupdate = Updateuserinfo(instance=request.user)
        customerupdate = Updatecustomerinfo(instance=request.user.customer)


    context = {'customerupdate': customerupdate, 'userupdate': userupdate}
    
    return render(request, 'store/profile.html', context)
    

    
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

class BookHotel (View):
    def get (self,request):
        htl_name = request.POST.get('hotel')
        htl_obj = Hotel.objects.filter(name = htl_name) #change
        price = {}
        return render(request, 'store/rooms.html', {'htl': htl_name, 'price': price})

    def post (self,request):
        htl_name = request.POST.get('hotel')
        print(htl_name)
        htl_obj = Hotel.objects.filter(name = htl_name) #change
        cust_obj = User.objects.filter(id = request.user.id)
        print(cust_obj)
        cust_obj = list(cust_obj)
        guests = []
        rooms = []
        #no_rooms = request.POST.get('select1')
        no_rooms = 2
        #no_rooms = int(no_rooms)
        #no_guests = request.POST.get('select2')
        no_guests = 2
        #no_guests = int(no_guests)
        price = 0
        type_room = request.POST.get('type')
        for htl in htl_obj:
            if (type_room == "Standard"):
                price = htl.price_std * no_rooms
            if (type_room == "Special"):
                price = htl.price_spl * no_rooms
            if (type_room == "Suite"):
                price = htl.price_suite * no_rooms
        for i in range (0,no_rooms):
            rooms.append(i+1)
        for j in range (0,no_guests):
            guests.append(i+1)

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
        

        if(name_1):
            htl_name = request.POST.get('hotel')
            print(htl_name)
            htl_obj = Hotel.objects.filter(name = htl_name)
            print(htl_obj)
            htl_objl = list(htl_obj)
            print(htl_obj)
            for htl in htl_objl:
                for cust in cust_obj:
                    room_save = Room(
                    hotel= htl,
                    user=cust,
                    #customer=cust,
                    gues1_name= name_1,
                    gues1_age = age_1,
                    gues1_gen = gender_1,
                    gues2_name= name_2,
                    gues2_age = age_2,
                    gues2_gen = gender_2,
                    gues3_name= name_3,
                    gues3_age = age_3,
                    gues3_gen = gender_3,
                    gues4_name= name_4,
                    gues4_age = age_4,
                    gues4_gen = gender_4,
                    gues5_name= name_5,
                    gues5_age = age_5,
                    gues5_gen = gender_5,
            )
                
            room_save.save()
            if (room_save):
                if (type_room == "Standard"):
                    for htl in htl_obj: #change flt_obj
                        num_stdrooms = htl.no_std -1
                        htl.save()
                if (type_room == "Special"):
                    for flt in htl_obj:
                        num_splrooms = htl.no_spl -1
                        htl.save()
                if (type_room == "Suite"):
                    for flt in htl_obj:
                        num_suites = htl.no_suites -1
                        #num_rooms = num_rooms - no_std - no_spl - no_suites
                        htl.save()
                return render(request, 'store/roomdetails.html', {'rooms': room_save, 'hotel': htl_obj, 'type': type_room})
            

        return render(request, 'store/rooms.html', {'guests': guests, 'type': type_room, 'price': price})


@permission_required('admin.can_add_log_entry')
def flights_upload(request):
    template = "store/flightsupload.html"

    prompt = {
        'order': 'Order of CSV should be airline, code, duration, price_e, price_b, price_fc, time, fromdest, todest, ns, nsle, nslb, nslf, obw, baggage_lim, apt_name, no_stops, stop_name'
    }

    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['file']

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)

    for column in csv.reader(io_string, delimiter = ','):
        _, created = Flights.objects.update_or_create(
           #id = column[0],
           airline = column[1],
           code = column[2],
           duration = column[3],
           price_e = column[4],
           price_b = column[5],
           price_fc = column[6],
           time = column[7],
           fromdest = column[8],
           todest = column[9],
           ns = column[10],
           nsle = column[11],
           nslb = column[12],
           nslf = column[13],
           obw = column[14],
           baggage_lim = column[15],
           apt_name = column[16],
           no_stops = column[17],
           stop_name = column[18], 
        )

    context={}
    return render(request, template, context)


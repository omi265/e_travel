from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def register(self):
        self.save()

    def __str__(self):
        #return f'{self.user.username}'
        return self.name
    
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()

"""
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""

class Airlines(models.Model):
    airline = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.airline

class Flights(models.Model):
    airline = models.ForeignKey('Airlines', on_delete=models.CASCADE)
    code = models.CharField(max_length=8, null=True)
    duration = models.CharField(max_length=20, null=True)
    price_e = models.IntegerField(default=5000)
    price_b = models.IntegerField(default=5000)
    price_fc = models.IntegerField(default=5000)
    time = models.DateTimeField()
    fromdest = models.CharField(max_length=20, null=True)
    todest = models.CharField(max_length=20, null=True)
    ns = models.IntegerField(null=True) #total number of seats 
    nsle = models.IntegerField(null=True) #number of seats left in economy
    nslb = models.IntegerField(null=True) #number of seats left in business
    nslf = models.IntegerField(null=True) #number of seats left in first class
    obw = models.CharField(max_length=3, null=True) #on-board wifi
    baggage_lim = models.IntegerField(null=True)
    apt_name = models.CharField(max_length=100, null=True)
    no_stops = models.IntegerField(default=0)
    stop_name = models.CharField(max_length=100, null=True)
    

    def __str__(self):
        return self.code

    @staticmethod
    def get_all_flights():
        return Flights.objects.all()

    class Meta:
        ordering = ['time']


class Location(models.Model):
    place = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.place

class Hotel(models.Model):
    place = models.ForeignKey('Location', on_delete=models.CASCADE)
    address = models.CharField(max_length=300, null=True)
    name = models.CharField(max_length=20, null=True)
    no_std = models.IntegerField(null=True)
    no_spl = models.IntegerField(null=True)
    no_suite = models.IntegerField(null=True)
    price_std = models.IntegerField(null=True)
    price_spl = models.IntegerField(null=True)
    price_suite = models.IntegerField(null=True)
    stars = models.FloatField(default=4.0)
    pets = models.CharField(max_length=10, null=True)
    wifi = models.CharField(max_length=10, null=True)
    pool = models.CharField(max_length=10, null=True)
    parking = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_hotels():
        return Hotel.objects.all()

    class Meta:
        ordering = ['name']


class Ticket(models.Model):
    flight = models.ForeignKey(Flights, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    pas1_name = models.CharField(max_length=50, null=True)
    pas1_age = models.IntegerField(null=True)
    pas1_gen = models.CharField(max_length=10, null=True)
    pas2_name = models.CharField(max_length=50, null=True)
    pas2_age = models.IntegerField(null=True)
    pas2_gen = models.CharField(max_length=10, null=True)
    pas3_name = models.CharField(max_length=50, null=True)
    pas3_age = models.IntegerField(null=True)
    pas3_gen = models.CharField(max_length=10, null=True)
    pas4_name = models.CharField(max_length=50, null=True)
    pas4_age = models.IntegerField(null=True)
    pas4_gen = models.CharField(max_length=10, null=True)
    pas5_name = models.CharField(max_length=50, null=True)
    pas5_age = models.IntegerField(null=True)
    pas5_gen = models.CharField(max_length=10, null=True)

    
#    def get_by_cust(customer):
#            return Ticket.objects.filter(customer__in = customer)
    @staticmethod
    def get_by_user(user):
        return Ticket.objects.filter(user__in = user )


# class Details(models.Model):
#     ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
#     pas_name = models.CharField(max_length=50, null=True)
#     pas_age = models.IntegerField(null=True)
#     pas_gen = models.CharField(max_length=10, null=True)
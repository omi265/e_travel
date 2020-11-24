from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username
        #return self.name

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Customer.objects.create(user=instance)
    #instance.profile.save()

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
    price = models.IntegerField(default=5000)
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
    name = models.CharField(max_length=20, null=True)
    stars = models.IntegerField()
    pets = models.CharField(max_length=10, null=True)
    cpn = models.IntegerField() #cost per night   

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_hotels():
        return Hotel.objects.all()

    class Meta:
        ordering = ['name']


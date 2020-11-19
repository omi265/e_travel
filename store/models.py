from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class Airlines(models.Model):
    airline = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.airline

class Flights(models.Model):
    airline = models.ForeignKey('Airlines', on_delete=models.CASCADE)
    #airline = models.CharField(max_length=20, null=True)
    code = models.CharField(max_length=8, null=True)
    duration = models.CharField(max_length=20, null=True)
    price = models.IntegerField(default=5000)
    time = models.DateTimeField()
    fromdest = models.CharField(max_length=20, null=True)
    todest = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.code

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


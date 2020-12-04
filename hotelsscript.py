import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_travel.settings')
django.setup()

import csv
from store.models import Hotel, Location
#import datetime

with open(r'C:\Users\manya\Desktop\Hotels.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    place = Location.objects.get(place=row['place'])
    temp = Hotel()
    temp.place = place
    temp.address = row['address']
    temp.img_1 = row['img_1']
    temp.img_2 = row['img_2']
    temp.name = row['name']
    temp.numrooms = int(row['numrooms'])
    temp.no_std = int(row['no_std'])
    temp.no_spl = int(row['no_spl'])
    temp.no_suite = int(row['no_suite'])
    temp.price_std = int(row['price_std'])
    temp.price_spl = int(row['price_spl'])
    temp.price_suite = int(row['price_suite'])
    temp.stars = int(row['stars'])
    temp.pets = row['pets']
    temp.wifi = row['wifi']
    temp.pool = row['pool']
    temp.parking = row['parking']
    
    temp.save()
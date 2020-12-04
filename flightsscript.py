import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'e_travel.settings')
django.setup()

import csv
from store.models import Flights, Airlines
#import datetime

with open(r'C:\Users\manya\Desktop\Flights.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    airline_ = Airlines.objects.get(airline=row['airline'])
    temp = Flights()
    temp.airline = airline_
    temp.code = row['code']
    temp.duration = row['duration']
    temp.price_e = int(row['price_e'])
    temp.price_b = int(row['price_b'])
    temp.price_fc = int(row['price_fc'])
    #temp.time = datetime(row['time'])
    temp.time = row['time']
    temp.fromdest = row['fromdest']
    temp.todest = row['todest']
    temp.ns = int(row['ns'])
    temp.nsle = int(row['nsle'])
    temp.nslb = int(row['nslb'])
    temp.nslf = int(row['nslf'])
    temp.obw = row['obw']
    temp.baggage_lim = int(row['baggage_lim'])
    temp.apt_name = row['apt_name']
    temp.no_stops = int(row['no_stops'])
    temp.stop_name = row['stop_name']

    temp.save()
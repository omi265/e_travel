from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'store/home.html')

# Create your views here.

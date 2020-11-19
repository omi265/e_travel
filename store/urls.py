from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights', views.all_flights, name='flights'),
    path('hotels', views.all_hotels, name='hotels'),
    # path('signup', views.Signup.as_view(), name='signup'),
    # path('login', views.Login.as_view(), name='login'),
    # path('logout', views.logout, name='logout'),
]

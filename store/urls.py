from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights', views.AllFlights.as_view(), name='flights'),
    path('hotels', views.all_hotels, name='hotels'),
    # path('signup', views.Signup.as_view(), name='signup'),
    path('login/', views.loginpage, name='login'),
    # path('logout', views.logout, name='logout'),
]

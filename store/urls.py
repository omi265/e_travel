from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights', views.AllFlights.as_view(), name='flights'),
    path('hotels', views.AllHotels.as_view(), name='hotels'),
    # path('signup', views.Signup.as_view(), name='signup'),
    path('login/', views.loginpage, name='login'),
    path('profile/', views.profilepage, name='profile'),
    # path('logout', views.logout, name='logout'),
]

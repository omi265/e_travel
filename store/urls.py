from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights', views.all_flights, name='flights'),
    path('hotels', views.all_hotels, name='hotels'),
    # path('signup', views.Signup.as_view(), name='signup'),
    path('login/', views.loginpage, name='login'),
    path('profile/', views.profilepage, name='profile'),
    # path('logout', views.logout, name='logout'),
]

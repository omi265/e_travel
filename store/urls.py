from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights', views.AllFlights.as_view(), name='flights'),
    path('hotels', views.AllHotels.as_view(), name='hotels'),
    path('book', views.BookFlts.as_view(), name='book'),
    path('history', views.history, name='history'),
    # path('filter', views.Filter.as_view(), name='filter'),
    # path('signup', views.Signup.as_view(), name='signup'),
    path('login/', views.loginpage, name='login'),
    path('profile/', views.profilepage.as_view(), name='profile'),
    # path('logout', views.logout, name='logout'),
]

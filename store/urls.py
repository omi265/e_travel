from django.urls import path, include
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('flights', views.AllFlights.as_view(), name='flights'),
    path('hotels', views.AllHotels.as_view(), name='hotels'),
    path('book', views.BookFlts.as_view(), name='book'),
    path('rooms', views.BookHotel.as_view(), name='rooms'),
    path('history', views.history, name='history'),
    path('rec', views.flt_hotels, name='rec'),
    path('rate', views.rate, name='rate'),
    # path('filter', views.Filter.as_view(), name='filter'),
    # path('signup', views.Signup.as_view(), name='signup'),
    path('login/', views.loginpage, name='login'),
    path('profile/', views.profilepage, name='profile'),
    # path('logout', views.logout, name='logout'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

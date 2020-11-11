from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup', views.Signup.as_view(), name='signup'),
    # path('login', views.Login.as_view(), name='login'),
    # path('logout', views.logout, name='logout'),
]

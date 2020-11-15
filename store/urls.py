from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('signup', views.Signup.as_view(), name='signup'),
    path('login/', views.loginpage, name='login'),
    # path('logout', views.logout, name='logout'),
]

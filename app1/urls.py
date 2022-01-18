from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.mainfun,name='main'),
    path('signup/',views.fnsignup,name='signup'),
    path('login/',views.fnlogin,name='login'),
    path('viewproductmain/',views.fnviewproductmain,name='viewproductmain'),


]
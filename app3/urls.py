from django.urls import path
from django.urls.conf import include
from . import views 

urlpatterns = [
    path('',views.fnmaster1,name='client'),
    path('home/',views.fnhome,name='home'),
    path('product/',views.fnproduct,name='product'),
    path('myservice/',views.fnmyservice,name='myservice'),
    path('fnlogoutclient/',views.fnlogoutclient,name='fnlogoutclient'),
    path('bookfullservice/',views.fnbookfullservice,name='bookfullservice'),
    path('savebookfullservice/',views.fnsavebookfullservice,name='savebookfullservice'),
    path('viewBookings/',views.fnviewBookings,name='viewBookings'),
    path('myservice/<custid>',views.fnmyservice,name='myservice'),
    path('loadclt/',views.fnloadclt,name='loadclt'),
    path('bookwaterserv/',views.fnbookwaterserv,name='bookwaterserv'),
    path('savewatrbook/',views.fnsavewatrbook,name='savewatrbook'),
    path('mywaterservice/<custwid>',views.fnmywaterservice,name='mywaterservice'),
]
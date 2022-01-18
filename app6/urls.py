from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.fnwaterhm,name='waterhm'),
    path('logoutwater/',views.fnlogoutwater,name='logoutwater'),
    path('viewwaterbooking/',views.fnviewwaterbooking,name='viewwaterbooking'),
    path('AcceptWaterRequest/<bkid>',views.fnAcceptWaterRequest,name='AcceptWaterRequest'),
    path('viewwatercustomer/',views.fnviewwatercustomer,name='viewwatercustomer'),
]
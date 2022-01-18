from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.fnmaster,name=''),
    path('overview/',views.fnover,name='overview'),
    path('addworkshop/',views.fnaddworkshop,name='addworkshop'),
    path('viewemployee/',views.fnviewemp,name='viewemployee'),
    path('viewcustomeradmin/',views.fnviewcustadmin,name='viewcustomeradmin'),
    path('customerfeedback/',views.fncustfeed,name='customerfeedback'),
    path('viewworkshop/',views.fnviewworkshop,name='viewworkshop'),
    path('viewTerminatedWorkshop/',views.fndeletedworkshop,name='viewTerminatedWorkshop'),
    path('viewpayment/',views.fnviewpayment,name='viewpayment'),
    path('viewproducts/',views.fnviewproduct,name='viewproducts'),
    path('viewproductrating',views.fnviewproductrating,name='viewproductrating'),
    path('viewterminatedemployee/',views.fndeletedemp,name='viewterminatedemployee'),
    path('addemp',views.fnaddemployees,name='addemp'),
    path('viewworkshopmsg',views.fnviewworkshop,name='viewworkshopmsg'),
    path('viewempmsg',views.fnviewemp,name='viewempmsg'),
    path('viewcustmsg',views.fnviewcust,name='viewcustmsg'),
    path('load/',views.fnloaddata,name='load'),
    path('viewworkshops/',views.fnViewWorkshop,name='viewworkshops'),
    path('saveworkshop/',views.fnsaveworkshop,name='saveworkshop'),
    path('deleteworkshop/',views.fndeleteworkshop,name='deleteworkshop'),
    path('fnlogoutadmin/',views.fnlogoutadmin,name='fnlogoutadmin'),
    path('loadempadmin/',views.fnloaddataemp,name='loadempadmin'),
    path('viewemployees/',views.fnViewEmp,name='viewemployees'),
    path('saveemp/',views.fnsaveemployee,name='saveemp'),
    path('deleteemp/',views.fndeleteemp,name='deleteemp'),
    path('addwaterservice/',views.fnaddwaterservice,name='addwaterservice'),
    path('viewwaterservice/',views.fnViewwaterservice,name='viewwaterservice'),
    path('editwaterservice/<watereditid>',views.fneditwaterservice,name='editwaterservice'),
    path('saveeditwaterservice/',views.fnsaveeditwaterservice,name='saveeditwaterservice'),
    path('delwaterservice/<watereditid>',views.fndelwaterservice,name='delwaterservice'),
    path('terminatedwaterservice/',views.fnterminatedwaterservice,name='terminatedwaterservice'),



]
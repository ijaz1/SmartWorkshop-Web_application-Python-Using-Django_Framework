from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.fnmaster3,name=''),
    path('homeemployee/',views.fnhomeemployee,name='homeemployee'),
    path('viewempworkshop/',views.fnempworkshopview,name='viewempworkshop'),
    path('addworkshopemp/',views.fnaddworkshopemp,name='addworkshopemp'),
    path('loademp/',views.fnloaddataemp,name='loademp'),
    path('viewworkshopsemp/',views.fnViewWorkshopemp,name='viewworkshopsemp'),
    path('saveworkshopemp/',views.fnsaveworkshopemp,name='saveworkshopemp'),
    path('deleteworkshopemp/',views.fndeleteworkshopemp,name='deleteworkshopemp'),
    path('fnlogoutemplo/',views.fnlogoutemplo,name='fnlogoutemplo'),
    path('addadverticement/',views.fnaddadverticement,name='addadverticement'),
    path('viewadverticehtml/',views.fnviewadverticehtml,name='viewadverticehtml'),
    path('viewadvertice/',views.fnviewadvertice,name='viewadvertice'),
    path('viewadverticement/',views.fnviewadverticement,name='viewadverticement'),
    path('saveadvertcementchange/',views.fnsaveadvertcementchange,name='saveadvertcementchange'),
    path('deladvertisement/',views.fndeladvertisement,name='deladvertisement'),   
    path('editabout/',views.fneditabout,name='editabout'),   
    path('deletedworkshopemp/',views.fndeletedworkshopemp,name='deletedworkshopemp'),  
    path('editcontactus/',views.fneditcontactus,name='editcontactus'),
    path('custfeedback/',views.fncustfeedback,name='custfeedback'),
    path('custeditfeedback/',views.fnviewcustfeedback,name='custeditfeedback'),
    path('custdeletefeedback/<delid>',views.fndeletecustfeedback,name='custdeletefeedback'),
    path('addwaterserviceemp/',views.fnaddwaterservice,name='addwaterserviceemp'),
    path('viewwaterserviceemp/',views.fnViewwaterservice,name='viewwaterserviceemp'),
    path('editwaterserviceemp/<watereditid>',views.fneditwaterservice,name='editwaterserviceemp'),
    path('saveeditwaterserviceemp/',views.fnsaveeditwaterservice,name='saveeditwaterserviceemp'),
    path('delwaterserviceemp/<watereditid>',views.fndelwaterservice,name='delwaterserviceemp'),
    path('terminatedwaterserviceemp/',views.fnterminatedwaterservice,name='terminatedwaterserviceemp'),
    path('addproduct/',views.fnaddproduct,name='addproduct'),
    path('viewproduct/',views.fnviewproduct,name='viewproduct'),
    path('editpro/<proid>',views.fneditpro,name='editpro'),
    path('saveeditedpro/',views.fnsaveeditedpro,name='saveeditedpro'),
    path('delpro/<prodid>',views.fndelpro,name='delpro'),


    


]
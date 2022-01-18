from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('',views.fnmaster2,name='master2'),
    path('homeemp',views.fnhomeemp,name='homeemp'),
    path('rejected',views.fnrejected,name='rejected'),
    path('viewcustomer',views.fnviewcustomer,name='viewcustomer'),
    path('viewpendingcustomers',views.fnviewpendingcustomers,name='viewpendingcustomers'),
    path('viewfinishedwork',views.fnviewfinishedwork,name='viewfinishedwork'),
    path('viewpayments',views.fnviewpayments,name='viewpayments'),
    path('viewrating',views.fnviewrating,name='viewrating'),
    path('viewfeedbacks',views.fnviewfeedbacks,name='viewfeedbacks'),
    path('viewfeedbacks',views.fnviewfeedbacks,name='viewfeedbacks'),
    path('fnlogoutworkshop/',views.fnlogoutworkshop,name='fnlogoutworkshop'),
    path('bookinkrequest/',views.fnbookinkrequest,name='bookinkrequest'),
    path('acceptrequest/<cid>',views.fnacceptrequest,name='acceptrequest'),
    path('cust1/<custid>',views.fncust1,name='cust1'),
    path('expected/',views.fnexpected,name='expected'),
    path('insert/',views.fninsert,name='insert'),
    path('load/',views.fnload,name='load'),
    path('finishedworklist/',views.fnfinishedworklist,name='finishedworklist'),
    path('viewcustomer/',views.fnviewcustomer,name='viewcustomer'),

]
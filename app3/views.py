from multiprocessing import context
from urllib import request
from django.core.checks import messages
from django.shortcuts import redirect, render
from app1.models import signuptb
from app3.models import fullServiceBooking, waterServBooking
from app5.models import CustFeedback, cotactus, aboutus
from app2.models import addworkshop, addwaterservice
from app4.models import Customer, Expected, liveValue, FinishedWorkList
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse

from app6.models import AcceptedwaterServ


def fnmaster1(request):
    return render(request, 'home.html')


def fnhome(request):
    obshowfeedback = CustFeedback.objects.all()
    obcontactuss = cotactus.objects.get(id=1)
    objshowabout = aboutus.objects.get(id=6)
    context = {'showcon': obcontactuss,
               'showfeedback': obshowfeedback, 'showabt': objshowabout}
    return render(request, 'home.html', context)


def fnproduct(request):
    return render(request, 'product.html')


def fnlogoutclient(request):
    del request.session['clt']
    return redirect('main')


def fnbookfullservice(request):
    obshwoworkshop = addworkshop.objects.all()
    context = {'showWorkshop': obshwoworkshop}
    return render(request, 'fullservice.html', context)


def fnsavebookfullservice(request):
    if request.method == 'POST':
        bname = request.POST['bname']
        mname = request.POST['mname']
        myear = request.POST['myear']
        purpose = request.POST['purpose']
        contact = request.POST['contact']
        ocomplaint = request.POST['ocomplaint']
        address = request.POST['address']
        zip = request.POST['zip']
        workshop = request.POST['workshop']
        clid = request.session['clt']
        ob = signuptb.objects.get(id=clid)
        fullServiceBooking(BrandName=bname, ModelName=mname, ManufacturedYear=myear, Purpose=purpose, Contact=contact, OtherComplaints=ocomplaint,
                           Address=address, zip=zip, WorkshopId=workshop, DateAndTime=datetime.now(), clid=clid, email=ob.email).save()
        messages.success(
            request, 'You Have Requested You Will Get A Confirmation Call')
        return redirect('bookfullservice')
    return redirect('bookfullservice')


def fnviewBookings(request):
    obviewcust = Customer.objects.all()
    obviewwater = AcceptedwaterServ.objects.all()
    context = {'viewcust': obviewcust, 'viewwater': obviewwater}
    return render(request, 'mybookings.html', context)


def fnmyservice(request, custid):
    try:
        obdetails = Customer.objects.get(id=custid)
        context = {'obdetails': obdetails}
        return render(request, 'myservice.html', context)
    except Exception as e:
        print(e)


def fnloadclt(request):
    try:
        get_id = request.GET['custid']
        obexpect = Expected.objects.get(cuid=get_id)
        load_obexpect = [{'id': obexpect.id, 'estimate': obexpect.estimatedprice,
                          'st': obexpect.st, 'et': obexpect.et, 'cuid': obexpect.cuid}]
        obviewlive = liveValue.objects.get(bookingId=get_id)
        load_obviewlive = [
            {'id': obviewlive.id, 'name': obviewlive.name, 'bookingId': obviewlive.bookingId}]
        obfinishedwork = FinishedWorkList.objects.filter(cuid=get_id)
        load_obfinishedwork = [{'id': i.id, 'FinishedWork': i.FinishedWork, 'ProductName': i.ProductName,
                                'TimeTaken': i.TimeTaken, 'Price': i.Price}for i in obfinishedwork]
        return JsonResponse({"expectdata": load_obexpect, "livevalue": load_obviewlive, "finishedWork": load_obfinishedwork})
    except Exception as e:
        print(e)


def fnbookwaterserv(request):
    objWater = addwaterservice.objects.all()
    context = {'waterserv': objWater}
    return render(request, 'waterservice.html', context)


def fnsavewatrbook(request):
    if request.method == 'POST':
        try:
            vehicle = request.POST['vehicle']
            cartype = request.POST['cartype']
            servtype = request.POST['servtype']
            contactno = request.POST['contactno']
            print('contact', contactno)
            ocomplaint = request.POST['ocomplaint']
            address = request.POST['address']
            zip = request.POST['zip']
            watershopid = request.POST['watershop']
            cid = request.session['clt']
            print('client id',cid)
            ob = signuptb.objects.get(id=cid)
            waterServBooking(vehicle=vehicle, cartype=cartype, servtype=servtype, contact=contactno, ocomplaint=ocomplaint,
                             address=address, zip=zip, watershopid=watershopid, clientid=cid, email=ob.email, DateAndTime=datetime.now()).save()
            messages.success(
                request, 'You Have Requested You Will Get A Confirmation Call')
            return redirect('bookwaterserv')
        except Exception as e:
            print(e)
    return redirect('bookwaterserv')


def fnmywaterservice(request, custwid):
    try:
        obdetails = AcceptedwaterServ.objects.get(id=custwid)
        context = {'obwdetails': obdetails}
        return render(request, 'mywaterservice.html', context)
    except Exception as e:
        print(e)

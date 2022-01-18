from multiprocessing import context
from unittest import removeResult
from django.shortcuts import redirect, render
from app1.models import signuptb
from app3.models import fullServiceBooking
from app2.models import addworkshop
from app4.models import Customer, Expected, FinishedWorkList, liveValue
from django.core.mail import send_mail
from django.conf import settings
from p1.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.http import JsonResponse
import json


def fnmaster2(request):
    return render(request, 'homeemp.html')


def fnhomeemp(request):
    wid = request.session['work']
    obcount = fullServiceBooking.objects.filter(WorkshopId=wid).count()
    context = {'obcount': obcount}
    return render(request, 'homeemp.html', context)


def fnviewbooking(request):
    return render(request, 'viewbooking.html')


def fnrejected(request):
    return render(request, 'rejected.html')


def fnviewpendingcustomers(request):
    return render(request, 'viewpendingcustomers.html')


def fnviewfinishedwork(request):
    return render(request, 'viewfinishedwork.html')


def fnviewpayments(request):
    return render(request, 'viewpayments.html')


def fnviewrating(request):
    return render(request, 'viewrating.html')


def fnviewfeedbacks(request):
    return render(request, 'viewfeedbacks.html')


def fnlogoutworkshop(request):
    del request.session['work']
    return redirect('main')


def fnbookinkrequest(request):
    try:
        wid = request.session['work']
        obbk = fullServiceBooking.objects.filter(WorkshopId=wid)
        print(obbk)
        print('io')
        context = {'shreq': obbk}
        return render(request, 'viewbooking.html', context)
    except Exception as e:
        print(e)
    return render(request, 'viewbooking.html')


def fnacceptrequest(request, cid):
    try:
        ob = fullServiceBooking.objects.get(id=cid)
        clem = ob.clid
        em = signuptb.objects.get(id=clem)
        print('client id ', em.firstname)
        email = em.email
        send_mail(
            'Your Request is Accepted',
            'we will contact you and time',
            'muhammedijazkari168@gmail.com',
            [email],
            fail_silently=False,
        )
        Customer(BrandName=ob.BrandName, ModelName=ob.ModelName, ManufacturedYear=ob.ManufacturedYear, Purpose=ob.Purpose, Contact=ob.Contact, OtherComplaints=ob.OtherComplaints,
                 Address=ob.Address, zip=ob.zip, WorkshopId=ob.WorkshopId, DateAndTime=ob.DateAndTime, clid=ob.clid, email=ob.email, CustomerName=em.firstname).save()
        obliveval = Customer.objects.get(BrandName=ob.BrandName)
        liveValue(name='Start Soon', bookingId=obliveval.id).save()
        fullServiceBooking.objects.filter(id=cid).delete()
        messages.success(request, 'Request Accepted')
        return redirect('viewwaterbooking')
    except Exception as e:
        print(e)


def fnviewcustomer(request):
    obviewcust = Customer.objects.all()
    context = {'viewcust': obviewcust}
    return render(request, 'viewcustomer.html', context)


def fncust1(request, custid):
    try:
        print('hey', custid)

        obdetails = Customer.objects.get(id=custid)
        print('hey', custid)
        # obexpected=Expected.objects.get(cuid=custid)
        print('hey', custid)
        context = {'obdetails': obdetails}
        return render(request, 'cust1.html', context)
    except Exception as e:
        print(e)


def fnexpected(request):
    esprice = request.POST['estimatedprice']
    st = request.POST['st']
    et = request.POST['et']
    cuid = request.POST['cuid']
    Expected(estimatedprice=esprice, st=st, et=et, cuid=cuid).save()
    return JsonResponse({"msg1": "Expected successfully"})


def fninsert(request):
    try:
        cuid = request.POST['cuid']
        name = request.POST['name']
        liveValue.objects.filter(bookingId=cuid).update(name=name)
        return JsonResponse({'msg': 'updated successfully'})
    except Exception as e:
        print(e)


def fnload(request):
    try:
        get_id = request.GET['cuid']
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


def fnfinishedworklist(request):
    cuid = request.POST['cuid']
    FinishedWork = request.POST['FinishedWork']
    ProductName = request.POST['ProductName']
    TimeTaken = request.POST['TimeTaken']
    Price = request.POST['Price']
    FinishedWorkList(cuid=cuid, FinishedWork=FinishedWork,
                     ProductName=ProductName, TimeTaken=TimeTaken, Price=Price).save()
    return JsonResponse({'msgadd': 'Added Successfully'})

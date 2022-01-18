from django.shortcuts import redirect, render
from app3.models import waterServBooking
from app1.models import signuptb
from app6.models import AcceptedwaterServ, LiveValueWater
from p1.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.


def fnwaterhm(request):
    return render(request, 'waterhome.html')


def fnlogoutwater(request):
    del request.session['water']
    return redirect('main')


def fnviewwaterbooking(request):
    try:
        wid = request.session['water']
        obbk = waterServBooking.objects.filter(watershopid=wid)
        context = {'shreqw': obbk}
        return render(request, 'viewbookingwater.html', context)
    except Exception as e:
        print(e)
    return render(request, 'viewbookingwater.html')


def fnAcceptWaterRequest(request, bkid):
    print('iiii')
    try:
        ob = waterServBooking.objects.get(id=bkid)
        print('idd', ob.id)
        clem = ob.clientid
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
        AcceptedwaterServ(vehicle=ob.vehicle, cartype=ob.cartype, servtype=ob.servtype, contact=ob.contact, ocomplaint=ob.ocomplaint,
                          address=ob.address, zip=ob.zip, watershopid=ob.watershopid, email=ob.email, clientid=ob.clientid, DateAndTime=ob.DateAndTime).save()
        obliveval = AcceptedwaterServ.objects.get(email=ob.email)
        LiveValueWater(valuewater='Start Soon', bookingId=obliveval.id).save()
        waterServBooking.objects.filter(id=bkid).delete()
        messages.success(request, 'Request Accepted')
        return redirect('bookinkrequest')
    except Exception as e:
        print(e)

def fnviewwatercustomer(request):
    obviewwatercust = AcceptedwaterServ.objects.all()
    context = {'viewwatercust': obviewwatercust}
    return render(request, 'viewwatercust.html', context)


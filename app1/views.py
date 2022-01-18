from django.contrib import messages
from django.shortcuts import redirect, render
from app1.models import signuptb
from . models import *
from app5.models import advertisement,aboutus, cotactus,addproduct
from app2.models import addemployees, addwaterservice,addworkshop

# Create your views here.
    
def mainfun(request):
    obcontactuss=cotactus.objects.get(id=1)
    objshowadd=advertisement.objects.all()
    objshowabout=aboutus.objects.get(id=6)
    obwat=addworkshop.objects.all()
    obwater=addwaterservice.objects.all()
    context={'showcon':obcontactuss,'advertise':objshowadd,'showabt':objshowabout,'showworkshop':obwat,'showwater':obwater}
    return render(request,'index.html',context)

def fnsignup(request):
    if request.method=='POST':
        email=request.POST['email']
        obj=signuptb.objects.filter(email=email).exists()
        objemp=addemployees.objects.filter(employeeemail=email).exists()
        objwork=addworkshop.objects.filter(workshopemail=email).exists()
        objwaterserv=addwaterservice.objects.filter(email=email).exists()
        if obj==False and objemp==False and objwork==False and objwaterserv==False:
            firstname=request.POST['firstname']
            print(firstname)
            lastname=request.POST['lastname']
            print(lastname)
            phonenumber=request.POST['phonenumber']
            print(phonenumber)
            email=request.POST['email']
            print(email)
            password=request.POST['password']
            print(password)
            obj1=signuptb(firstname=firstname,lastname=lastname,phonenumber=phonenumber,email=email,password=password)
            obj1.save()
            messages.success(request,'Account Created Successfully')
            return redirect('main')
        messages.error('Email already exist')
        return redirect('main')
    return redirect('main')

def fnlogin(request):
    if request.method=='POST':
        loginemail=request.POST['loginemail']
        loginpassword=request.POST['loginpassword']
        objemp=addemployees.objects.filter(employeeemail=loginemail).exists()
        objwork=addworkshop.objects.filter(workshopemail=loginemail).exists()
        objclient=signuptb.objects.filter(email=loginemail).exists()
        objwaterserv=addwaterservice.objects.filter(email=loginemail).exists()
        try:
            if loginemail=='admin@smart.com' and loginpassword=='1234':
                request.session['admin']='111'
                return redirect('overview')
            elif objemp==True:
                obchpassemp=addemployees.objects.get(employeeemail=loginemail,employeepassword=loginpassword)
                request.session['emp']=obchpassemp.id
                return redirect('homeemployee')
            elif objwork==True:
                obchpasswrk=addworkshop.objects.get(workshopemail=loginemail,workshoppassword=loginpassword)
                request.session['work']=obchpasswrk.id
                return redirect('homeemp')
            elif objwaterserv==True:
                obchpasswtr=addwaterservice.objects.get(email=loginemail,password=loginpassword)
                request.session['water']=obchpasswtr.id
                return redirect('waterhm')
            elif objclient==True:
                obchpassclt=signuptb.objects.get(email=loginemail,password=loginpassword)
                request.session['clt']=obchpassclt.id
                return redirect('home')
        except Exception as e:print(e)
        messages.error(request,'Password Is Wrong')
    return redirect('main')

def fnviewproductmain(request):
    objadpro=addproduct.objects.all()
    context={'viewpro':objadpro}
    return render(request,'viewProductmain.html',context)



    
    






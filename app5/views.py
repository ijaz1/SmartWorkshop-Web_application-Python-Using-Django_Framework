from django.shortcuts import redirect, render
from django.http import JsonResponse
from app2.models import addworkshop,deletedworkshop,addwaterservice,deletewaterservice
from app5.models import CustFeedback, addproduct, advertisement,aboutus, cotactus
from random import random
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
import os


def fnmaster3(request):
    return render(request,'master3.html')


def fnhomeemployee(request):
    obabout=aboutus.objects.get(id=6)
    obcontactus=cotactus.objects.get(id=1)
    context={'showabout':obabout,'showcontact':obcontactus}
    return render(request,'homeemployee.html',context)

def fnempworkshopview(request):
    return render(request,'viewworkshopemp.html')

def fnviewcustfeedback(request):
    obviewcustfeedback=CustFeedback.objects.all()
    context1={'viewcustfeed':obviewcustfeedback}
    return render(request,'editfeddback.html',context1)


def fnaddworkshopemp(request):
    if request.method=='POST':
        workshopemail=request.POST['workshopemail']
        obj3=addworkshop.objects.filter(workshopemail=workshopemail).exists()
        if obj3==False:
            workshopname=request.POST['workshopname']
            workshopplace=request.POST['workshopplace']
            phonenumber=request.POST['phonenumber']
            workshoppassword=request.POST['workshoppassword']
            workshopemail=request.POST['workshopemail']
            obj2=addworkshop(workshopname=workshopname,workshopplace=workshopplace,phonenumber=phonenumber,workshoppassword=workshoppassword,workshopemail=workshopemail)
            obj2.save()
            return render(request,'viewworkshopemp.html',{'msgaddemp':'successfull'})
        return render(request,'viewworkshopemp.html',{'msgaddemp':'unsuccessful'})
    return render(request,'viewworkshopemp.html')

def fnloaddataemp(request):
    obj=addworkshop.objects.all()
    load_obj=[{'id':i.id,'name':i.workshopname,'place':i.workshopplace,'phone':i.phonenumber,'email':i.workshopemail,'password':i.workshoppassword}for i in obj]
    return JsonResponse({'data':load_obj})

def fnViewWorkshopemp(request):
    uid=request.POST['user_id']
    objworkshop=addworkshop.objects.get(id=uid)
    viewobj=[{'id':objworkshop.id,'wname':objworkshop.workshopname,'wplace':objworkshop.workshopplace,'wphone':objworkshop.phonenumber,'wemail':objworkshop.workshopemail,'wpassword':objworkshop.workshoppassword}]
    return JsonResponse({'wdata':viewobj})

def fnsaveworkshopemp(request):
    wname1=request.POST['wname1']
    print(wname1)
    wplace1=request.POST['wplace1']
    wphone1=request.POST['wphone1']
    wemail1=request.POST['wemail1']
    wpassword1=request.POST['wpassword1']
    wid=request.POST['wid']
    addworkshop.objects.filter(id=wid).update(workshopname=wname1,workshopplace=wplace1,phonenumber=wphone1,workshopemail=wemail1,workshoppassword=wpassword1)
    return JsonResponse({'msg':'updated succesfully'})
    
    
def fndeleteworkshopemp(request):
    widd=request.POST['wid11']
    objaddworkshopdel=addworkshop.objects.get(id=widd)
    objworkdelsave=deletedworkshop(id=objaddworkshopdel.id,workshopname=objaddworkshopdel.workshopname,workshopplace=objaddworkshopdel.workshopplace,phonenumber=objaddworkshopdel.phonenumber,workshopemail=objaddworkshopdel.workshopemail,workshoppassword=objaddworkshopdel.workshoppassword)
    objworkdelsave.save()
    addworkshop.objects.filter(id=widd).delete()
    return JsonResponse({'delmsg':'deleted successfully'})

def fnlogoutemplo(request):
    del request.session['emp']
    return redirect('main')

def fnaddadverticement(request):
    photo=request.FILES['photo']
    flphoto=str(random())+photo.name
    objphoto=FileSystemStorage()
    objphoto.save(flphoto,photo)
    mainhead=request.POST['mainhead']
    fsubhead=request.POST['fsubhead']
    ssubhead=request.POST['ssubhead']
    objsave=advertisement(photo=flphoto,mainhead=mainhead,fsubhead=fsubhead,ssubhead=ssubhead)
    objsave.save()
    return render(request,'homeemployee.html',{'msgadvertisement':'inserted succesfully'})
    
def fnviewadverticehtml(request):
    return render(request,'viewad.html')

def fnviewadvertice(request):
    try:
        obadget=advertisement.objects.all()
        obadshow=[{'id':i.id,'photo':i.photo,'mainhead':i.mainhead,'fsubhead':i.fsubhead,'ssubhead':i.ssubhead}for i in obadget]
        return JsonResponse({'shoad':obadshow})
    except Exception as e:print(e)

def fnviewadverticement(request):
    advid=request.POST['adv_id']
    obadvtb=advertisement.objects.get(id=advid)
    obadtbpost=[{'id':obadvtb.id,'photo':obadvtb.photo,'mainhead':obadvtb.mainhead,'fsubhead':obadvtb.fsubhead,'ssubhead':obadvtb.ssubhead}]
    return JsonResponse({'shobad':obadtbpost})

def fnsaveadvertcementchange(request):
    mhead=request.POST['mainhead1']
    fshead=request.POST['fsubhead1']
    sshead=request.POST['ssubhead1']
    cid=request.POST['aid']
    advertisement.objects.filter(id=cid).update(mainhead=mhead,fsubhead=fshead,ssubhead=sshead)
    return JsonResponse({'msg':'updated succesfully'})

def fndeladvertisement(request):
    advid=request.POST['adid11']
    advertisement.objects.filter(id=advid).delete()
    return JsonResponse({'delmsg':'deleted successfully'})


def fneditabout(request):
    abouttext=request.POST['abouttextarea']
    aboutus.objects.update(abouttext=abouttext)
    messages.success(request,'edited succesfully')
    return redirect('homeemployee')

def fndeletedworkshopemp(request):
    objdelworkshopshaow=deletedworkshop.objects.all()
    return render(request,'viewterminatedworkshopemp.html',{'deletedworkshop':objdelworkshopshaow})

def fneditcontactus(request):
    phone=request.POST['phone']
    email=request.POST['email']
    whatsapp=request.POST['whatsapp']
    cotactus.objects.update(phone=phone,email=email,whatsapp=whatsapp)
    messages.success(request,'Contact us updated succesfully')
    return redirect('homeemployee')
def fncustfeedback(request):
    custfeedphoto=request.FILES['custfeedphoto']
    flcustfeedphoto=str(random())+custfeedphoto.name
    objcustfeedphoto=FileSystemStorage()
    objcustfeedphoto.save(flcustfeedphoto,custfeedphoto)
    CustFeedback(photo=flcustfeedphoto).save()
    messages.success(request,'Feedback added succesfully')
    return redirect('homeemployee')

def fndeletecustfeedback(request,delid):
    CustFeedback.objects.filter(id=delid).delete()
    messages.success(request,'feedback Deleted Succesfully')
    return redirect('custeditfeedback')

def fnaddwaterservice(request):
    if request.method=='POST':
        wateremail=request.POST['wateremail']
        obj3=addwaterservice.objects.filter(email=wateremail).exists()
        if obj3==False:
            watername=request.POST['watername']
            waterplace=request.POST['waterplace']
            waternumber=request.POST['waternumber']
            wateremail=request.POST['wateremail']
            waterpassword=request.POST['waterpassword']
            obj2=addwaterservice(name=watername,place=waterplace,phonenumber=waternumber,email=wateremail,password=waterpassword)
            obj2.save()
            messages.success(request,'Workshop Added Succesfully')
            return redirect('viewwaterserviceemp')
        messages.success(request,'Email Already Exist')
        return redirect('viewwaterserviceemp')
    return redirect('viewwaterserviceemp')

def fnViewwaterservice(request):
    objviewwaterservice=addwaterservice.objects.all()
    context={'waterservice':objviewwaterservice}
    return render(request,'viewwaterservemp.html',context)

def fneditwaterservice(request,watereditid):
    print('ijas')
    objeditview=addwaterservice.objects.get(id=watereditid)
    contextt={'geteditvalue':objeditview}
    return render(request,'editwaterservemp.html',contextt)

def fnsaveeditwaterservice(request):
    if request.method=='POST':
        waterserviceid=request.POST['waterserviceid']
        name=request.POST['wsname']
        place=request.POST['wsplace']
        number=request.POST['wsnumber']
        email=request.POST['wsemail']
        password=request.POST['wspassword']
        addwaterservice.objects.filter(id=waterserviceid).update(name=name,place=place,phonenumber=number,email=email,password=password)
        messages.success(request,'updated successfully')
        return redirect('viewwaterserviceemp')

def fndelwaterservice(request,watereditid):
    objsavedeletews=addwaterservice.objects.get(id=watereditid)
    deletewaterservice(name=objsavedeletews.name,place=objsavedeletews.place,phonenumber=objsavedeletews.phonenumber,email=objsavedeletews.email,password=objsavedeletews.password).save()
    addwaterservice.objects.filter(id=watereditid).delete()
    messages.success(request,'Deleted successfully')
    return redirect('viewwaterserviceemp')

def fnterminatedwaterservice(request):
    obdelwaterserv=deletewaterservice.objects.all()
    return render(request,'viewterminatedwaterservemp.html',{'obdelwaterserv':obdelwaterserv})

def fnaddproduct(request):
    if request.method=='POST':
        productphoto=request.FILES['productphoto']
        productname=request.POST['productname']
        productprice=request.POST['productprice']
        stock=request.POST['status']
        addproduct(photo=productphoto,name=productname,price=productprice,stock=stock).save()
        messages.success(request,'product added successfully')
        return redirect('homeemployee')
    return redirect('homeemployee')

def fnviewproduct(request):
    objadpro=addproduct.objects.all()
    context={'viewpro':objadpro}
    return render(request,'viewProduct.html',context)


def fneditpro(request,proid):
    objeditproview=addproduct.objects.get(id=proid)
    contextt={'geteditvaluepro':objeditproview}
    return render(request,'editproduct.html',contextt)

def fnsaveeditedpro(request):
    if request.method=='POST':
        proeditid=request.POST['proeditid']
        pro=addproduct.objects.get(id=proeditid)
        if len(request.FILES) != 0:
            if len(pro.photo) > 0:
                os.remove(pro.photo.path)
            pro.photo = request.FILES['image']
        pro.name=request.POST['productname']
        pro.price=request.POST['productprice']
        pro.stock=request.POST['status']
        pro.save()
        messages.success(request,'Updated Successfully')
        return redirect('viewproduct')

def fndelpro(request,prodid):
    addproduct.objects.filter(id=prodid).delete()
    messages.success(request,'Deleted successfully')
    return redirect('viewproduct')

    




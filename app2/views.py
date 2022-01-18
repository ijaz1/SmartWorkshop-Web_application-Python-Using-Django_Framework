from typing import Counter
from django.http.response import JsonResponse
from django.shortcuts import redirect, render

from app2.models import addemployees, addwaterservice, addworkshop, deletedworkshop,deletedemployees, deletewaterservice
from app1.models import signuptb
from django.http import JsonResponse
from django.contrib import messages

from app5.models import cotactus

def fnmaster(request):
    return render(request,'master.html')

def fnover(request):
    return render(request,'overview.html')

def fnviewemp(request):
    return render(request,'viewemployee.html')

def fnviewcust(request):
    return render(request,'viewcustomers.html')

def fncustfeed(request):
    return render(request,'customerfeedback.html')

def fnviewworkshop(request):
    return render(request,'viewworkshop.html')

def fnviewpayments(request):
    return render(request,'viewpayment.html')

def fndeletedworkshop(request):
    return render(request,'viewterminatedworkshop.html')

def fnviewpayment(request):
    return render(request,'viewpayment.html') 

def fnviewproduct(request):
    return render(request,'viewproducts.html') 

def fnviewproductrating(request):
    return render(request,'viewproductrating.html')        

def fndeletedemp(request):
    return render(request,'viewterminatedemployee.html')   

def fnviewemp(request):
    return render(request,'viewemployee.html') 

def fnaddemployees(request):
    if request.method=='POST':
        employeeemail=request.POST['employeeemail']
        obj=addemployees.objects.filter(employeeemail=employeeemail).exists()
        if obj==False:
            employeefullname=request.POST['employeefullname']
            employeeplace=request.POST['employeeplace']
            employeephonenumber=request.POST['employeephonenumber']
            employeepassword=request.POST['employeepassword']
            employeeemail=request.POST['employeeemail']
            salary=request.POST['salary']
            obj1=addemployees(employeefullname=employeefullname,employeeemail=employeeemail,employeeplace=employeeplace,employeephonenumber=employeephonenumber,employeepassword=employeepassword,salary=salary)
            obj1.save()
            return render(request,'overview.html',{'msgaddemp':'successfull'})
        return render(request,'overview.html',{'msgaddemp':'unsuccessful'})
    return render(request,'overview.html')

def fnaddworkshop(request):
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
            return render(request,'overview.html',{'msgaddemp':'successfull'})
        return render(request,'overview.html',{'msgaddemp':'unsuccessful'})
    return render(request,'overview.html')

def fnviewworkshop(request):
    objwkshop=addworkshop.objects.all()
    return render(request,'viewworkshop.html',{'viewworkshopmsg':objwkshop})

def fnviewemp(request):
    objviewemp=addemployees.objects.all()
    return render(request,'viewemployee.html',{'viewempmsg':objviewemp})

def fnviewcustadmin(request):
    objviewcust=signuptb.objects.all()
    return render(request,'viewcustomers.html',{'viewcustmsg':objviewcust})


def fnloaddata(request):
    obj=addworkshop.objects.all()
    load_obj=[{'id':i.id,'name':i.workshopname,'place':i.workshopplace,'phone':i.phonenumber,'email':i.workshopemail,'password':i.workshoppassword}for i in obj]
    return JsonResponse({'data':load_obj})

def fnViewWorkshop(request):
    uid=request.POST['user_id']
    objworkshop=addworkshop.objects.get(id=uid)
    viewobj=[{'id':objworkshop.id,'wname':objworkshop.workshopname,'wplace':objworkshop.workshopplace,'wphone':objworkshop.phonenumber,'wemail':objworkshop.workshopemail,'wpassword':objworkshop.workshoppassword}]
    return JsonResponse({'wdata':viewobj})

def fnsaveworkshop(request):
    wname1=request.POST['wname1']
    print(wname1)
    wplace1=request.POST['wplace1']
    wphone1=request.POST['wphone1']
    wemail1=request.POST['wemail1']
    wpassword1=request.POST['wpassword1']
    wid=request.POST['wid']
    addworkshop.objects.filter(id=wid).update(workshopname=wname1,workshopplace=wplace1,phonenumber=wphone1,workshopemail=wemail1,workshoppassword=wpassword1)
    return JsonResponse({'msg':'updated succesfully'})
    
    
def fndeleteworkshop(request):
    widd=request.POST['wid11']
    objaddworkshopdel=addworkshop.objects.get(id=widd)
    objworkdelsave=deletedworkshop(id=objaddworkshopdel.id,workshopname=objaddworkshopdel.workshopname,workshopplace=objaddworkshopdel.workshopplace,phonenumber=objaddworkshopdel.phonenumber,workshopemail=objaddworkshopdel.workshopemail,workshoppassword=objaddworkshopdel.workshoppassword)
    objworkdelsave.save()
    addworkshop.objects.filter(id=widd).delete()
    return JsonResponse({'delmsg':'deleted successfully'})

def fnlogoutadmin(request):
    del request.session['admin']
    return redirect('main')

def fnloaddataemp(request):
    objemp=addemployees.objects.all()
    load_objemp=[{'id':i.id,'name':i.employeefullname,'place':i.employeeplace,'phone':i.employeephonenumber,'email':i.employeeemail,'password':i.employeepassword,'salary':i.salary,}for i in objemp]
    return JsonResponse({'empdata':load_objemp})

def fnViewEmp(request):
    eid=request.POST['emp_id']
    objemploye=addemployees.objects.get(id=eid)
    viewempobj=[{'id':objemploye.id,'ename':objemploye.employeefullname,'eplace':objemploye.employeeplace,'ephone':objemploye.employeephonenumber,'eemail':objemploye.employeeemail,'epassword':objemploye.employeepassword,'salary':objemploye.salary}]
    return JsonResponse({'edata':viewempobj})

def fnsaveemployee(request):
    ename1=request.POST['ename1']
    print(ename1)
    eplace1=request.POST['eplace1']
    ephone1=request.POST['ephone1']
    eemail1=request.POST['eemail1']
    epassword1=request.POST['epassword1']
    esalary1=request.POST['esalary1']
    eid=request.POST['eid']
    addemployees.objects.filter(id=eid).update(employeefullname=ename1,employeeplace=eplace1,employeephonenumber=ephone1,employeeemail=eemail1,employeepassword=epassword1,salary=esalary1)
    return JsonResponse({'msg':'updated succesfully'})

def fndeleteemp(request):
    eid1=request.POST['eid1']
    objdeleemp=addemployees.objects.get(id=eid1)
    objdeleempsave=deletedemployees(id=objdeleemp.id,employeefullname=objdeleemp.employeefullname,employeeplace=objdeleemp.employeeplace,employeephonenumber=objdeleemp.employeephonenumber,employeeemail=objdeleemp.employeeemail,employeepassword=objdeleemp.employeepassword)
    objdeleempsave.save()
    addemployees.objects.filter(id=eid1).delete()
    return JsonResponse({'delmsg':'deleted successfully'})

def fndeletedworkshop(request):
    objdelworkshopshaow=deletedworkshop.objects.all()
    return render(request,'viewterminatedworkshop.html',{'deletedworkshop':objdelworkshopshaow})

def fndeletedemp(request):
    objdelempshow=deletedemployees.objects.all()
    return render(request,'viewterminatedemployee.html',{'delempshow':objdelempshow})

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
            return redirect('viewwaterservice')
        messages.success(request,'Email Already Exist')
        return redirect('viewwaterservice')
    return redirect('viewwaterservice')

def fnViewwaterservice(request):
    objviewwaterservice=addwaterservice.objects.all()
    context={'waterservice':objviewwaterservice}
    return render(request,'viewwaterservicecenter.html',context)

def fneditwaterservice(request,watereditid):
    print('ijas')
    objeditview=addwaterservice.objects.get(id=watereditid)
    contextt={'geteditvalue':objeditview}
    return render(request,'editwaterservicecenter.html',contextt)

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
        return redirect('viewwaterservice')

def fndelwaterservice(request,watereditid):
    objsavedeletews=addwaterservice.objects.get(id=watereditid)
    deletewaterservice(name=objsavedeletews.name,place=objsavedeletews.place,phonenumber=objsavedeletews.phonenumber,email=objsavedeletews.email,password=objsavedeletews.password).save()
    addwaterservice.objects.filter(id=watereditid).delete()
    messages.success(request,'Deleted successfully')
    return redirect('viewwaterservice')

def fnterminatedwaterservice(request):
    obdelwaterserv=deletewaterservice.objects.all()
    return render(request,'viewterminatedwaterservice.html',{'obdelwaterserv':obdelwaterserv})



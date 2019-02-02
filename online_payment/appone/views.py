from django.shortcuts import render,render_to_response,HttpResponseRedirect,HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.
from django.shortcuts import render ,get_object_or_404,redirect
from .form import createCustomerForm,loginCustomerForm
from .models import customer,currentbill,paidCurrent,unpaidCurrent,accountinfo
#Email+registratio
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from .token import activation_token
from django.db import connection
from datetime import datetime


def home(request):
    return render(request,"appone/index11.html")

def getregislogin(request):
    return render(request,"appone/regislogin.html")


def getregister(request):
    form = createCustomerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instancex = form.save(commit=False)

        passwordd = form.cleaned_data['password']

        instancex.password = make_password(password=passwordd,
                                      salt=None,
                                      hasher='unsalted_md5')

        instancex.active = False
        #nicher line ta just apatoto..ata pore change kora hobe
        instancex.userid= 0

        instancex.save()
        site = get_current_site(request)
        mail_subject= "Confirmation message for Bill.com"
        messaage= render_to_string('appone/confirmationMail.html',{
            'user' : instancex,
            'domain' : site.domain,
            'uid': instancex.id,
            'token': activation_token.make_token(instancex)

        })
        to_mail = form.cleaned_data.get('email')
        to_list = [to_mail]
        from_mail = settings.EMAIL_HOST_USER
        send_mail(mail_subject, messaage, from_mail, to_list , fail_silently=True)
        return HttpResponse("<h1> Thank you Forr Your registration. A confirmation Link has been sent to your email</h1>")
        return render(request, "appone/index11.html")

    return render(request, "appone/register.html", {"form": form})


def getlogin(request):
    email="test"
    form = loginCustomerForm(request.POST or None)
    if form.is_valid():

        passwordd = form.cleaned_data['password']
        emaill = form.cleaned_data['email']

        passworddd = make_password(password=passwordd,
                                   salt=None,
                                   hasher='unsalted_md5')

        # user = get_object_or_404(customer, email=emaill,password=passworddd)
        user = customer.objects.filter(email=emaill, password=passworddd, active=True)
        if (user):
            #request.session['user']=emaill


            response = HttpResponseRedirect('/')
            response.set_cookie('user', emaill)
            #response.set_cookie('cookie_name2', 'cookie_name2_value')
            return response
            #response.set_cookie('user',emaill)
            #return response

        else:
            return redirect('regislogin')

    return render(request, "appone/login.html", {"form": form})

def getlogout(request):
    response = HttpResponseRedirect('login')
    response.delete_cookie('user')
    response.delete_cookie('cookie_name2')
    return response


def getconfirmation(request,uid,token):
    try:
        user=get_object_or_404(customer,pk=uid)
    except:
        raise HttpResponse("No User found")
    if user is not None and activation_token.check_token(user,token):
        user.active=True
        user.save()
        return HttpResponse("<h1>Your Acount Has been Done. You can <a href='/login'>Login </a>  </h1>")
    else:
        return HttpResponse("<h2> Invalid Link </h3>")




def getbillpay(request):
    if request.method == "POST":
        billno = request.POST.get('billno')
        accountno = request.POST.get('accountno')
        user1= get_object_or_404(currentbill, billno=billno)
        user2=get_object_or_404(customer,account_no=accountno)
        if user1.userid != user2.userid:
            return HttpResponse("<h1>Your Acount Has been Done. You can <a href='/billpay'> Try Again </a>  </h1>")
        else:
            billtable=unpaidCurrent.objects.filter(billno=billno)
            context={
                "billtablee" : billtable,
                "show" : 1
            }
            request.session['bill'] = billno
            request.session['account'] = accountno

            return render(request,"appone/billpay.html", context)


    return render(request,"appone/billpay.html")



def getgocheckbox(request):
    if request.method == "POST":
        billno = request.POST.get('billno')
        accountno = request.POST.get('accountno')
        user1= get_object_or_404(currentbill, billno=billno)
        user2=get_object_or_404(customer,account_no=accountno)
        if user1.userid != user2.userid:
            return HttpResponse("<h1>Your Acount Has been Done. You can <a href='/billpay'> Try Again </a>  </h1>")
        else:
            billtable=unpaidCurrent.objects.filter(billno=billno)
            context={
                "billtablee" : billtable,
                "show" : 1
            }
            return render(request,"appone/checkboxesPage.html", context)


    return render(request,"appone/checkboxesPage.html")

def  getshowcheckboxResult(request):
    if request.method == 'POST':
        # gives list of id of inputs
        ids = []
        ids = request.POST.getlist('inputs')
        #or....
        #for p in id:
           #ids=unpaidCurrent.objects.filter(amount=p)


        context={
                "idd" : ids
        }
        return render(request,"appone/showCheckboxResult.html",context)

def getsubmitchoice(request):
    if request.method == 'GET':
        amount=request.GET.get('amount')
        mas=request.GET.get('mas')
        context={
            "mass": mas,
            "amountt":amount
        }

        return render(request,"appone/accpassinput.html",context)

    if request.method == 'POST':
        cursor = connection.cursor()

        mas = request.POST.get('mas')
        accpass = request.POST.get('accpass')
        amountt = request.POST.get('amount')

        amounttt=int(amountt)

        accountid = request.session['account']
        billid = request.session['bill']

        check_person = accountinfo.objects.filter(account_no=accountid, account_password=accpass)
        if check_person.count() == 0:
            return HttpResponse("<h1> Wrong Password </h1>")
        else:
            #cursor = connection.cursor()
            cursor.execute("SELECT * FROM appone_accountinfo WHERE account_no=%s AND amount > %s", [accountid,amounttt])
            row = cursor.fetchone()
            # will return as a touple  print(row[0])... print(row[1])
            # print(row[2])
            if row:
                #print(row[2])
                current_balance=row[2]

                #print(current_balance)
                new_balance=int(current_balance)-amounttt
                #print(new_balance)
                
                inst=paidCurrent(billno=billid,month=mas,amount=amounttt)
                inst.save()

                dlt=unpaidCurrent.objects.filter(billno=billid,month=mas)
                dlt.delete()

                cursor.execute("UPDATE appone_accountinfo SET  amount = %s WHERE account_no= %s",[new_balance,accountid])

                return HttpResponse("<h1> Going</h1")




def getbalancecheck(request):
    if request.method == 'POST':
        mas=request.POST.get('mas')
        accpass=request.POST.get('accpass')
        amountt=request.POST.get('amount')

        accountid=request.session['account']
        billid=request.session['bill']

        check_person=accountinfo.objects.filter(account_no=accountid,account_password=accpass)
        if check_person.count() == 0:
            return HttpResponse("<h1> Wrong Password </h1>")
        else:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM appone_accountinfo WHERE appone_accountinfo.amount > %s",[amountt])
            row=cursor.fetchone()
            #will return as a touple  print(row[0])... print(row[1])
            #print(row[2])
            if row:
                print("done")



        return HttpResponse("<h1>goin</h1>")


def getgoajax(request):
    return render(request, "appone/inputajax.html")

def getajaxbillshow(request):
    if request.method=="POST":
        accountno=request.POST['accountno']
        billno=request.POST['billno']

        user1 = get_object_or_404(currentbill, billno=billno)
        user2 = get_object_or_404(customer, account_no=accountno)

        if user1.userid == user2.userid:
            billtable1 = unpaidCurrent.objects.filter(billno=billno)
            billtable12=paidCurrent.objects.filter(billno=billno)
            context = {
                "billtablee": billtable1,
                "billtableee":billtable12

            }
            request.session['bill'] = billno
            request.session['account'] = accountno

            return render(request, "appone/showajax.html", context)


    else:
        return HttpResponse("<h1>show ajax</h1>")





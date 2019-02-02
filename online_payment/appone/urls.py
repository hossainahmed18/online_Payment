"""online_payment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from appone import views
from appone.views import home
from appone.views import getregislogin
from appone.views import getregister
from appone.views import getlogin
from appone.views import getlogout
from appone.views import getconfirmation
from appone.views import getbillpay
from appone.views import getgocheckbox
from appone.views import getshowcheckboxResult
from appone.views import getbalancecheck
from appone.views import getsubmitchoice
from appone.views import getgoajax
from appone.views import getajaxbillshow

urlpatterns = [

  path('',home,name='home'),
  path('regislogin', getregislogin, name='regislogin'),
  path('register', getregister, name='register'),
  path('login', getlogin, name='login'),
  path('logout', getlogout, name='logout'),
  path('succesLogin/<uid>/<token>',  getconfirmation, name='succesLogin'),
  path('billpay', getbillpay, name='billpay'),
  path('gocheckbox', getgocheckbox, name='gocheckbox'),
  path('showcheckboxResult', getshowcheckboxResult, name='showcheckboxResult'),
  path('balacecheck', getbalancecheck, name='balacecheck'),
  path('submitchoice', getsubmitchoice, name='submitchoice'),

  path('goajax', getgoajax, name='goajax'),
  path('ajaxbillshow', getajaxbillshow, name='ajaxbillshow'),


]
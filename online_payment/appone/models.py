# Create your models here.
from django.db import models


# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(default="")
    phone = models.CharField(max_length=30, null=True, blank=True)
    image = models.FileField(null=True, blank=True)
    account_no = models.CharField(max_length=30)
    password = models.CharField(max_length=300)
    active = models.BooleanField(default=False)
    userid=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class currentbill(models.Model):
    userid=models.IntegerField(default=0)
    billno=models.CharField(max_length=30)

    def __str__(self):
        return self.billno


class accountinfo(models.Model):
    account_no = models.CharField(max_length=30)
    amount = models.IntegerField()
    account_password=models.CharField(max_length=30)

    def __str__(self):
        return self.account_no

class unpaidCurrent(models.Model):
   billno=models.CharField(max_length=30)
   month = models.CharField(max_length=50)
   amount = models.IntegerField()

   def __str__(self):
        return self.billno


class paidCurrent(models.Model):
    billno = models.CharField(max_length=30)
    month = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid_on = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.billno



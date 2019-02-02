# Register your models here.
from django.contrib import admin
from .models import customer,currentbill,accountinfo,paidCurrent,unpaidCurrent


# Register your models here.

class customerModel(admin.ModelAdmin):
    list_display = ["__str__", "account_no","email","phone"]

    class Meta:
        model = customer

admin.site.register(customer, customerModel)


class currentModel(admin.ModelAdmin):
    list_display = ["__str__","userid"]

    class Meta:
        model = currentbill

admin.site.register(currentbill, currentModel)


class accountinfoModel(admin.ModelAdmin):
    list_display = ["__str__", "amount"]

    class Meta:
        model = accountinfo

admin.site.register(accountinfo, accountinfoModel)


class paidCurrentModel(admin.ModelAdmin):
    list_display = ["__str__","month","amount","paid_on"]

    class Meta:
        model = paidCurrent

admin.site.register(paidCurrent,paidCurrentModel)


class unpaidCurrentModel(admin.ModelAdmin):
    list_display = ["__str__", "month", "amount"]

    class Meta:
        model = unpaidCurrent


admin.site.register(unpaidCurrent, unpaidCurrentModel)

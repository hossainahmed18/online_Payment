from django import forms
from .models import customer

class createCustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = [

            'name',
            'email',
            'phone',
            'image',
            'account_no',
            'password'


        ]

class loginCustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = [


            'email',
            'password'

        ]

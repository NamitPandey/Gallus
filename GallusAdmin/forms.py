from django import forms
from ROOT.models import *


class ProjectForm(forms.ModelForm):
    class Meta():

        model = Products_List

        fields = [
            'product_name',
            'product_type',
            'product_description',
            'price',
        ]

        widgets = {

            'product_name':forms.TextInput(attrs={
                                    'class':'textinputclass', 'required': True,
                                    }
                                    ),
            'product_type':forms.Select(attrs={ 'required': True}),
            'product_description':forms.Textarea(attrs={'required': True}),
            'price':forms.NumberInput(attrs={'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.fields['product_name'].label = 'Product Name'
        self.fields['product_description'].label = 'Product Description'
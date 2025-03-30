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


class WelcomeForm(forms.ModelForm):
    class Meta():

        model = ViewManager

        fields = [
            'banner_type',
            'banner_title',
            'title_text',
        ]

        widgets = {

            'banner_title':forms.TextInput(attrs={
                                    'class':'form-control',"name":"banner_title", "id":"id_banner_title exampleInputUsername1",'required': True
                                    }
                                    ),
            'banner_type':forms.Select(attrs={'class':'form-control',"name":"banner_type", "id":"id_banner_type exampleInputUsername1",'required': True}),
            'title_text':forms.Textarea(attrs={'class':'form-control',"name":"title_text", "id":"id_title_text exampleInputUsername1",'required': True}),
        }

    def __init__(self,choiceVal=None, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['banner_title'].label = 'Title'
        self.fields['banner_type'].label = 'Type'
        self.fields['title_text'].label = 'Discription'
        if choiceVal != None:
            banner_type_text = choiceVal["banner_type"]
            banner_type_title = choiceVal["banner_title"]
            title_text = choiceVal["title_text"]
            self.fields["banner_type"].choices = [(f"{banner_type_text}",f"{banner_type_text.replace('_',' ')}")]
            self.initial["banner_title"] = f"{banner_type_title}"
            self.initial["title_text"] = f"{title_text}"

        
class FeedbackForm(forms.ModelForm):
    class Meta():

        model = ViewManager

        fields = [
            'banner_type',
            'title_text',
            "client_company",
            'feedback_by',        
            ]

        widgets = {

            'banner_type':forms.Select(attrs={'class':'form-control', "id":"id_banner_type exampleInputUsername1"}),
            'title_text':forms.Textarea(attrs={'class':'form-control', "id":"id_title_text exampleInputUsername1"}),
            'client_company':forms.TextInput(attrs={'class':'form-control', "id":"id_client_company exampleInputUsername1"}),
            'feedback_by':forms.TextInput(attrs={'class':'form-control', "id":"id_feedback_by exampleInputUsername1"}),

        }
    
    def __init__(self,choiceVal=None, *args, **kwargs):

        super().__init__(*args, **kwargs)
        # self.fields['banner_title'].label = 'Title'
        self.fields['banner_type'].label = 'Type'
        self.fields['title_text'].label = 'Discription'
        self.fields['banner_type'].required = False
        self.fields['title_text'].required = False
        self.fields['client_company'].required = False
        self.fields['feedback_by'].required = False
        
        if choiceVal != None:
            banner_type_text = choiceVal["banner_type"]
            title_text = choiceVal["title_text"]
            client_company = choiceVal["client_company"]
            feedback_by = choiceVal["feedback_by"]
            self.fields["banner_type"].choices = [(f"{banner_type_text}",f"{banner_type_text.replace('_',' ')}")]
            self.initial["title_text"] = f"{title_text}"
            self.initial["client_company"] = f"{client_company}"
            self.initial["feedback_by"] = f"{feedback_by}"

class AboutUsForm(forms.ModelForm):
    class Meta():

        model = ViewManager

        fields = [
            # 'banner_type',
            'banner_title',
            'title_text',
        ]

        widgets = {

            'banner_title':forms.TextInput(attrs={
                                    'class':'form-control','required': True
                                    }
                                    ),
            # 'banner_type':forms.Select(attrs={'class':'form-control','required': True}),
            'title_text':forms.Textarea(attrs={'class':'form-control','required': True}),
        }

    def __init__(self,choiceVal=None, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.fields['banner_title'].label = 'Title'
        # self.fields['banner_type'].label = 'Type'
        self.fields['title_text'].label = 'Discription'
        if choiceVal != None:
            # banner_type_text = choiceVal["banner_type"]
            banner_type_title = choiceVal["banner_title"]
            title_text = choiceVal["title_text"]
            # self.fields["banner_type"].choices = [(f"{banner_type_text}",f"{banner_type_text.replace('_',' ')}")]
            self.initial["banner_title"] = f"{banner_type_title}"
            self.initial["title_text"] = f"{title_text}"
            
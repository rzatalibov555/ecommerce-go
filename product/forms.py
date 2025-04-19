
from django import forms
from .models import Product

# https://www.youtube.com/watch?v=MBbVq_FIYDA - super().__init__()
# https://www.youtube.com/watch?v=mcAB5dBXMp4 - *args и **kwargs

class ProductForm(forms.ModelForm):

    # description = forms.CharField(widget=forms.Textarea(attrs={'cols':40, 'rows':5}))
    
    class Meta:
        model = Product
        # fields = ("name", "price",)
        # fields = "__all__"
        exclude = ("time_create", "time_update","status", "image")
        widgets = {
            "description": forms.Textarea(attrs={'cols':20, 'rows':10}),
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs['class'] = "form-control"
    #     self.fields['description'].widget.attrs['class'] = "form-control"







# class ProductForm(forms.Form):
#     name = forms.CharField()
#     price = forms.CharField()
#     tax_price  = forms.CharField()

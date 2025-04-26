
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
    #     self.fields['price'].widget.attrs['class'] = "form-control"

    def __init__(self, *args, **kwargs):
       
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
         

    def clean(self):
        attrs = self.cleaned_data
        name = attrs.get("name")
        price = attrs.get("price")
        # print(name)
        if name.startswith("a"):
            raise forms.ValidationError("Ad a ile baslaya bilmez!")
        
        if price is not None and price < 1:
            raise forms.ValidationError("Qiymet 1den asagi ola bilmez!")
        return attrs


    # def save(self, commit = True):
    #     if commit:
    #         print("We are inside")
    #         return Product.objects.create(
    #             **self.cleaned_data
    #         )
    #     else:
    #         return Product(**self.cleaned_data)



# class ProductForm(forms.Form):
#     name = forms.CharField()
#     price = forms.CharField()
#     tax_price  = forms.CharField()

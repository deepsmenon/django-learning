from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
  title       = forms.CharField(label=" ",widget=forms.TextInput(attrs={"placeholder":"your title"}))
  email       = forms.EmailField()
  description = forms.CharField (
                required= False,
                widget=forms.Textarea(
                  attrs = {
                    "placeholder":"your title",
                    "class":"new-class-name two",
                    "id" :"my-id-for-text-area",
                    "row": 10,
                    'cols' : 1200

                  }
                )
  )
  price = forms.DecimalField(initial=100.9)
  class Meta:
    model = Products
    fields =[
      'title',
      'email',
      'description',
      'price'      
    ]
  def clean_title(self,*args,**kwargs):
    title = self.cleaned_data.get("title")
    if not "CFE" in title:
        raise forms.ValidationError("This is not a valid title")
    if not "news" in title:
        raise forms.ValidationError("This is not a valid title")
    return title
  def clean_email(self,*args,**kwargs):
    email = self.cleaned_data.get("email")
    if not email.endswith("edu"):
        raise forms.ValidationError("This is not a valid email")
    return email

class RawProductForm(forms.ModelForm):
  title       = forms.CharField(label=" ",widget=forms.TextInput(attrs={"placeholder":"your title"}))
  description = forms.CharField (
                required= False,
                widget=forms.Textarea(
                  attrs = {
                    "placeholder":"your title deepa",
                    "class":"new-class-name two",
                    "id" :"my-id-for-text-area",
                    "rows": 10,
                    'cols' : 120

                  }
                )
  )
  price = forms.DecimalField(initial=100.9)
  class Meta:
    model = Products
    fields =[
      'title',
      'Discription',
      'price'
      
    ]
  def clean_title(self,*args,**kwargs):
    title = self.cleaned_data.get("title")
    if not "CFE" in title:
        raise forms.ValidationError("This is not a valid title")
    if not "news" in title:
        raise forms.ValidationError("This is not a valid title")
    return title
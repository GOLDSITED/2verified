from django.forms import ModelForm, Textarea
from django import forms
from . models import Product



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','title','slug','description','price','old_price','is_featured', 'num_available','last_visit','image','thumbnail']
        widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'old_price': forms.TextInput(attrs={'class': 'form-control'}),
            'num_available': forms.TextInput(attrs={'class': 'form-control'}),
            'last_visit': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
        }

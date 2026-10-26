from django import forms
from .models import product,student,Document
class Contactform(forms.Form):
    name=forms.CharField(max_length=50)
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields="__all__"
    
class StudentForm(forms.ModelForm):
    class Meta:
        model =student
        fields = "__all__"

class DocumentForm(forms.ModelForm):
    class Meta:
        model=Document
        fields=["name","file"]
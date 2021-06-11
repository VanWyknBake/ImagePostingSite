from django import forms

class PostForm(forms.Form):
    title = forms.CharField()   
    image = forms.FileField()
    description = forms.CharField()
    

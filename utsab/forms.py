from django import forms

class User_form(forms.Form):
    name = forms.CharField( max_length=100)
    email = forms.EmailField()
    number = forms.IntegerField(max_value=100)
    message = forms.CharField(widget=forms.Textarea)
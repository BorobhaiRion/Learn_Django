from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    age = forms.IntegerField(min_value=0, label='Your Age')
    email = forms.EmailField(required=False, label='Your Email (optional)')
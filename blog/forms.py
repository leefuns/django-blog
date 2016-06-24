from django import forms

class contact(forms.Form):
	name = forms.CharField(max_length=10)
	email = forms.EmailField(required=False)
	message = forms.CharField(min_length=12)
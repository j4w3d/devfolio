from django import forms


class FormValidation(forms.Form):
     name = forms.CharField(min_length=4, max_length=50)
     email = forms.EmailField(required=True)
     subject = forms.CharField(min_length=8, max_length=127)
     message = forms.CharField(min_length=4, max_length=255)


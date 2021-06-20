from django import forms

class CompanyForm(forms.Form):
    name = forms.CharField()
    slug = forms.CharField()
    details = forms.CharField(widget=forms.Textarea)
from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(label='', max_length=100)


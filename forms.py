from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(label='Informe a URL', max_length=100)


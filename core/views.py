from django.shortcuts import render
from forms import UrlForm
from django.contrib import messages
import pyshorteners


def index(request):
    form = UrlForm(request.POST or None)
    url_encurtada = ''
    if str(request.method) == 'POST':
        if form.is_valid():
            link = pyshorteners.Shortener()
            try:
                url_encurtada = link.tinyurl.short(form.cleaned_data["url"])
                messages.success(request, 'URL Gerada Com Sucesso')
            except:
                messages.error(request, 'Não foi possível gerar a URL')
            form = UrlForm()
    context = {
        'form': form,
        'url_encurtada': url_encurtada,
    }
    return render(request, 'index.html', context)

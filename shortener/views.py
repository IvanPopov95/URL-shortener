from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UrlModel
from .forms import UrlForm
from avito import settings
from django.core.exceptions import ObjectDoesNotExist

def index_view(request):
    if request.method == 'POST':
        long_url = request.POST['original_url']
        form = UrlForm(request.POST)
        if form.is_valid(): 
        #    Для избежания дублирования в БД используется get_or_create
           url = UrlModel.objects.get_or_create(original_url=long_url)
           short_url = settings.SITE_NAME + encode(url[0].id)
           form = UrlForm()
           return render(request, 'avito_prj/index.html', {'form':form,
                                                            'short_url':short_url})
    else:     
        form = UrlForm()
        return render(request, 'avito_prj/index.html', {'form':form})

def encode(base10):
    base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    base62 = []

    while base10 > 0:
        val = base10 % 62
        base62.append(base[val])
        base10 //= 62

    return "".join(base62[::-1])

def decode_view(request, code):

    base = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    idx = []

    for i in range(len(code)):
        idx.append(base.index(code[i]))

    for i in range(len(idx)):
        idx[i] *= (62 ** (len(idx) - i - 1))
    try:
        url = UrlModel.objects.get(id=sum(idx))
    # если такой сокращенный URL не существует - вернет обратно на домашнюю страницу 
    except ObjectDoesNotExist:
        return redirect('index')
    
    return redirect(url.original_url)
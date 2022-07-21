from django.shortcuts import render
from django.http import HttpResponse
from .forms import leituraMedidor

def index(request):
    form = leituraMedidor(request.GET)

    context = {
        'form': form
    }

    return render(request, 'index.html', context=context)

def calcula(request):

    if(request.method == 'POST'):

        form = leituraMedidor(request.POST)

        if(form.is_valid()):
            leitura_atual = form.cleaned_data['leitura_atual']
            leitura_anterior = form.cleaned_data['leitura_anterior']

    return render(request, 'fatura.html')

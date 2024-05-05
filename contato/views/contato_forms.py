
from django.shortcuts import render
from contato.forms import ContatoForm

# Create your views here.


def create(request):
    if request.method == 'POST':
        context = {
        'form': ContatoForm(request.POST)
    }
        return render(request, 'contato/create.html', context)

    context = {
        'form': ContatoForm()
    }
    return render(request, 'contato/create.html', context)
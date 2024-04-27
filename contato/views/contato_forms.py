from django.shortcuts import render, get_object_or_404, redirect
from contato.models import Contato
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator
from django import forms


# Create your views here.

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = (
            'first_name', 'last_name0', 'phone',
                  )



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
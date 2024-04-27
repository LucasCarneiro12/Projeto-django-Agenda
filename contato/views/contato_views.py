from django.shortcuts import render, get_object_or_404, redirect
from contato.models import Contato
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    contatos = Contato.objects.filter(show=True).order_by('id')

    paginator = Paginator(contatos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, 
        'site_title': 'Contatos - '
    }

    return render(request, 'contato/index.html', context)


def search(request):
    search_value = request.GET.get('q', '').strip()

    if search_value == '':
        return redirect('contato:index')

    contatos = Contato.objects.filter(show=True)\
        .filter(Q(first_name__icontains=search_value) | Q(last_name0__icontains=search_value) | Q(phone__icontains=search_value) |
                Q(email__icontains=search_value))\
        .order_by('id')

    
    paginator = Paginator(contatos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj, 
        'site_title': 'Search - '
    }

    return render(request, 'contato/index.html', context)




def contato(request, contato_id):
   # single_contato = Contato.objects.filter(pk=contato_id).first()
    single_contato = get_object_or_404(Contato, pk=contato_id, show=True)

    site_title = f'{single_contato.first_name} {single_contato.last_name0} - '

    context = {
        'contato': single_contato, 
        'site_title': site_title,
    }

    return render(request, 'contato/contato.html', context)




from django.shortcuts import render, redirect, get_object_or_404
from contato.forms import ContatoForm
from django.urls import reverse
from contato.models import Contato
# Create your views here.


def create(request):

    form_action = reverse('contato:create')

    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES)
        context = {
        'form': form,
        'form_action': form_action,
    }
        if form.is_valid():
            contato = form.save()
            return redirect('contato:update', contato_id=contato.pk)

        return render(request, 'contato/create.html', context)

    context = {
        'form': ContatoForm(),
        'form_action': form_action,
    }
    return render(request, 'contato/create.html', context)




def update(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id, show=True)
    form_action = reverse('contato:update', args=(contato_id,))

    if request.method == 'POST':
        form = ContatoForm(request.POST, request.FILES, instance=contato)
        context = {
        'form': form,
        'form_action': form_action,
    }
        if form.is_valid():
            contato = form.save()
            return redirect('contato:update', contato_id=contato.pk)

        return render(request, 'contato/create.html', context)

    context = {
        'form': ContatoForm(instance=contato),
        'form_action': form_action,
    }
    return render(request, 'contato/create.html', context)




def delete(request, contato_id):
    contato = get_object_or_404(Contato, pk=contato_id, show=True)

    confirmation = request.POST.get('confirmation', 'no')
    print(' confirmation',  confirmation)
    if confirmation == 'yes':
        contato.delete()
        return redirect('contato:index')
    return render(
        request,
        'contato/contato.html',
        {
            'contato': contato,
            'confirmation': confirmation,
        }
    )
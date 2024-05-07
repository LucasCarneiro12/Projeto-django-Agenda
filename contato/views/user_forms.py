from django.shortcuts import render, redirect
from django.contrib import messages
from contato.forms import RegisterForm

def register(request):
    form = RegisterForm()

    messages.info(request, 'slaaar')
    messages.warning(request, 'slaaar')
    messages.error(request, 'slaaar')

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado')
            return redirect('contato:index')

    return render(
        request,
        'contato/register.html',
        {
            'form': form
        }
    )
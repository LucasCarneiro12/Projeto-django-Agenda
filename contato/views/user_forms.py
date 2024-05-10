from django.shortcuts import render, redirect
from django.contrib import messages, auth
from contato.forms import RegisterForm, ResgisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

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


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
           # messages.success('logado com sucesso')
            print(user)
            auth.login(request, user)
            return redirect('contato:index')
        else:
            messages.error(request, 'login inválido')

    return render(
        request, 
        'contato/login.html',
        {
            'form': form
        }
    )
@login_required(login_url='contato:login')
def user_update(request):
     form = ResgisterUpdateForm(instance=request.user)

     if request.method != 'POST':
         
        return render(
            request,
            'contato/user_update.html',
            {
                'form': form
            }
        )
     form = ResgisterUpdateForm(data=request.POST, instance=request.user)

     if not form.is_valid():
         return render(
            request,
            'contato/user_update.html',
            {
                'form': form
            }
        )
     form.save()
     return redirect('contato:user_update')

@login_required(login_url='contato:login')
def logout_view(request):
    auth.logout(request)
    return redirect('contato:login')
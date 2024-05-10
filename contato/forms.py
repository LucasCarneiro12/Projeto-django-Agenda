from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

class ContatoForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'classe-a classe-b', 'placeholder': "seu nome",}
        ), 
        label='primeiro nome',
        help_text="texto de ajuda para user",
    )
    # editei por conta proria
    last_name0 = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'classe-a classe-b', 'placeholder': "seu ultimo nome",}
        ), 
        label='Sobrenome',
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'classe-a classe-b',}
        ), 
        label='Telefone',
    )
    #até aqui

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*'
            }
        ), 
        required=False,
    )

    class Meta:
        model = models.Contato
        fields = (
            'first_name', 'last_name0', 'phone',
             'email', 'descripion', 'category', 'picture')
       # widgets = {
        #    'first_name': forms.TextInput(
         #       attrs={'class': 'classe-a classe-b', 'placeholder': "seu nome",}
          #  )
        #}
    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data == '123':
            self.add_error(
                'first_name',
                ValidationError(
                    'Mensagem de erro', code='invalid'
                )
                  )
    
        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if first_name == 'ABC':
            self.add_error('first_name', ValidationError('não digite ABC', code='invalid'))
        return first_name
    


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )

    last_name = forms.CharField(
        required=True,
        min_length=3,
    )

    email = forms.EmailField(
        required=True,
    )

    class Meta():
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )
        
        return email


class ResgisterUpdateForm(forms.ModelForm):
     first_name = forms.CharField(
         min_length=2,
         max_length=50,
         required=True,
         help_text='Required.',
         error_messages={
             'min_length': 'Por favor, adicione mais que duas letras.'
         }
        )
     last_name = forms.CharField(
         min_length=2,
         max_length=50,
         required=True,
         help_text='Required.',
        
     )

     password1 = forms.CharField(
         label="Password",
         strip=False,
         widget=forms.PasswordInput(attrs={"autocomplete": 'new-password'}),
         help_text=password_validation.password_validators_help_text_html(),
         required=False,
     )
     password2 = forms.CharField(
         label="Password",
         strip=False,
         widget=forms.PasswordInput(attrs={"autocomplete": 'new-password'}),
         help_text='User the same password as before.',
         required=False,
     )
     class Meta():
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
            )

     def save(self, commit=True):
         cleaned_data = self.cleaned_data   
         user = super().save(commit=False)

         password = cleaned_data.get('password1')

         if password:
             user.set_password(password)

         if commit:
             user.save()
         return user

     def clean(self):
         password1 = self.cleaned_data.get('password1')
         password2 = self.cleaned_data.get('password2')

         if password1 or password2:
             if password1 != password2:
                 self.add_error(
                     'password2',
                     ValidationError('senhas não batem')
                 )
         return super().clean()
     

     def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Já existe este e-mail', code='invalid')
                )
        
        return email
     
     def clean_password1(self):
         password1 = self.cleaned_data.get('password1')

         if not password1:
             try:
                 password_validation.validate_password(password1)
             except ValidationError as errors:
                 self.add_error(
                     'password1', 
                     ValidationError(errors)
                 )
        
         return password1
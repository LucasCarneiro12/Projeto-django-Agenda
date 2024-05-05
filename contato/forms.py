from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContatoForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'classe-a classe-b', 'placeholder': "seu nome",}
        ), 
        label='primeiro nome',
        help_text="texto de ajuda para user",
    )

 #   def __init__(self, **args, **kwargs):
  #      super().__init__(**args, **kwargs)
    class Meta:
        model = models.Contato
        fields = (
            'first_name', 'last_name0', 'phone',
             'email', 'descripion', 'category',     )
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
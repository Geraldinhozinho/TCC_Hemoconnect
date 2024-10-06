from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'email', 'senha', 'confir'] 
        #posso usar o '__all__' também
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Nome',
                'required': 'true'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Email',
                'required': 'true'
            }),
            'senha': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Senha',
                'required': 'true'
            }),
            'confir': forms.TextInput(attrs={
                'class': 'form-input', 
                'placeholder': 'Confirmar Senha',
                'required': 'true'
            }),
        }
from django import forms
from .models import Usuario, Questionario, Campanhas
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
import re


class FotoPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['foto_perfil']
        
class UsuarioForm(UserCreationForm):
    cpf = forms.CharField(max_length=14, required=True, help_text="Digite seu CPF sem pontos ou traços.")
    endereco = forms.CharField(max_length=255, required=False)
    nome_completo = forms.CharField(max_length=200, required=False)
    
    
    class Meta:
        model = Usuario
        fields = ('username', 'nome_completo', 'cpf', 'endereco', 'email', 'password1', 'password2')
        error_messages = {
            'username': {
                'max_length': 'O nome de usuário não pode exceder 150 caracteres.',
                'invalid': 'O nome de usuário contém caracteres inválidos.',
            },
            'nome_completo': {
                'max_length': 'O nome completo não pode exceder 200 caracteres.',
            },
            'cpf': {
                'max_length': 'O CPF deve ter no máximo 14 caracteres.',
                'invalid': 'Insira um CPF válido.',
            },
            'email': {
                'invalid': 'Insira um e-mail válido.',
            },
            'password1': {
                'password_too_similar': 'A senha é muito parecida com informações pessoais.',
                'password_too_short': 'A senha deve ter pelo menos 8 caracteres.',
                'password_too_common': 'A senha é muito comum.',
                'password_entirely_numeric': 'A senha não pode ser inteiramente numérica.',
            },
            'password2': {
                'password_mismatch': 'As senhas não correspondem.',
            },
        }
        
        widget={
        }
        
    def clean_nome_completo(self):
        nome_completo = self.cleaned_data['nome_completo']
        if not re.match(r'^[A-Za-zÀ-ÿ\s]+$', nome_completo):
            raise forms.ValidationError('Seu nome só pode conter letras e espaços.')
        return nome_completo
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Usuario.objects.filter(cpf=cpf).exists():
            raise ValidationError("Este CPF já está cadastrado.")
        return cpf

        
class QuestionarioForm(forms.ModelForm):
    doenca_det = forms.CharField(
        required=False,  # Não obrigatório, será validado dinamicamente
        widget=forms.TextInput(attrs={'class': 'doenca2-forms', 'placeholder': 'Digite o nome da doença'}),
    )

    class Meta:
        model = Questionario  # Modelo associado ao formulário
        fields = [
            'idade','querer', 'nome', 'email', 'tipo_sangue', 'fuma', 'sexo',
            'doenca', 'doenca_det', 'disponibilidade', 'dias'
        ]  # Inclua 'doenca_det' nos campos

        widgets = {
            'querer': forms.RadioSelect(attrs={'class': 'tornar-forms'}),
            'nome': forms.TextInput(attrs={'class': 'nome-forms', 'placeholder': 'Digite seu nome'}),
            'idade': forms.NumberInput(attrs={'class': 'nome-forms', 'placeholder': 'Digite sua idade'}),
            'email': forms.EmailInput(attrs={'class': 'email-forms', 'placeholder': 'Digite seu email'}),
            'tipo_sangue': forms.RadioSelect(attrs={'class': 'sangue-forms'}),
            'fuma': forms.RadioSelect(attrs={'class': 'fuma-forms'}),
            'sexo': forms.RadioSelect(attrs={'class': 'sexo-forms'}),
            'doenca': forms.RadioSelect(attrs={'class': 'doenca-forms'}),
            'disponibilidade': forms.RadioSelect(attrs={'class': 'disponibilidade-forms'}),
            'dias': forms.CheckboxSelectMultiple(attrs={'class': 'dias-forms'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        doenca = cleaned_data.get('doenca')
        doenca_det = cleaned_data.get('doenca_det')

        if doenca == 'Sim' and not doenca_det:
            self.add_error('doenca-det', 'Por favor, informe o nome da doença.')

            return cleaned_data
        
    

        
class CampanhasForm(forms.ModelForm):
    class Meta:
        model = Campanhas
        fields = ['titulo','descricao','image']
        
        widgets = {
            'titulo': forms.TextInput(attrs=({'class':'titulomodal'})),
            'descricao': forms.TextInput(attrs=({'class':'descricaomodal'})),           
        }

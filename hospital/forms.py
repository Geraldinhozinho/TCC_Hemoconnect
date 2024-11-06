from django import forms
from .models import Usuario, Questionario, Campanhas
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UsuarioForm(UserCreationForm):
    cpf = forms.CharField(max_length=11, required=True, help_text="Digite seu CPF sem pontos ou traços.")
    endereco = forms.CharField(max_length=255, required=False)
    nome_completo = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Usuario
        fields = ('username', 'nome_completo', 'cpf', 'endereco', 'email', 'password1', 'password2')
        
        widget={
            'username': forms.TextInput(attrs=({'placeholder': 'Digite seu nome'})),
        }

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if Usuario.objects.filter(cpf=cpf).exists():
            raise ValidationError("Este CPF já está cadastrado.")
        return cpf

        
class QuestionarioForm(forms.ModelForm):
    class Meta:
        model = Questionario
        fields = ['querer', 'nome', 'email', 'tipo_sangue', 'fuma', 'sexo', 'doenca', 'doenca_det', 'disponibilidade', 'dias']
        
        # Definir widgets personalizados para alguns campos
        widgets = {
            'querer': forms.RadioSelect(attrs=({'class':'quer'})),
            
            'nome': forms.TextInput(attrs=({'class':'nome','placeholder': 'Digite seu nome'})),
            
            'email': forms.TextInput(attrs=({'class':'nome','placeholder': 'Digite seu email'})),
            
            'tipo_sangue': forms.RadioSelect(attrs=({'class':'sangue'})),
            
            'fuma': forms.RadioSelect(attrs=({'class':'fuma'})),
            
           'sexo': forms.RadioSelect(attrs=({'class':'sexo'})),
           
           'doenca': forms.RadioSelect(attrs=({'class':'doenca'})),
           
           'doenca_det': forms.TextInput(attrs=({'class':'doenca2','placeholder': 'Digite aqui o nome da doença'})),
           
           'disponibilidade': forms.RadioSelect(attrs=({'class':'dispo'})),
           
           'dias': forms.CheckboxSelectMultiple(attrs=({'class':'dias'})),
           
        }
        
    def clean(self):
        cleaned_data = super().clean()
        doenca = cleaned_data.get('doenca')
        doenca_det = cleaned_data.get('doenca_det')

        # Se a resposta de 'doenca' for 'Sim', o campo 'doenca_det' deve ser obrigatório
        if doenca == 'sim' and not doenca_det:
            self.add_error('doenca_det', 'Por favor, informe a doença se você marcou "Sim".')
        
        return cleaned_data
        

        
class CampanhasForm(forms.ModelForm):
    class Meta:
        model = Campanhas
        fields = ['titulo','descricao','image']
        
        widgets = {
            'titulo': forms.TextInput(attrs=({'class':'titulomodal'})),
            'descricao': forms.TextInput(attrs=({'class':'descricaomodal'})),           
        }

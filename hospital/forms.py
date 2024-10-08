from django import forms
from .models import Usuario, Questionario 

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
        
        
        

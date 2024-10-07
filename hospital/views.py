from django.shortcuts import render,redirect
from .forms import UsuarioForm, QuestionarioForm
from .models import Usuario

# Create your views here.

def inicio(request):
     return render(request, 'hospital/tela_inicial.html')


from django.shortcuts import render, redirect
from .forms import UsuarioForm  # Certifique-se de que o formulário está importado corretamente

def cadastro(request):
     form = UsuarioForm()
     if request.method == 'POST':
          form = UsuarioForm(request.POST)
          if form.is_valid():
               form.save()  # Salva o usuário no banco de dados
               return redirect('tela_inicial')  # Redireciona para uma página de sucesso ou outra URL
     contexto = {
          'form': form  # O nome correto seria 'form' e não 'forms'
     }

     return render(request, 'hospital/tela_login1.html', contexto)


def login(request):
          
     return render(request, 'hospital/tela_inicial.html')



#QUESTIONARIO 2 
def questionario(request):
     form = QuestionarioForm()
     if request.method == 'POST':
          form = QuestionarioForm(request.POST)
          if form.is_valid():
               form.save()  # Salva o usuário no banco de dados
               return redirect('tela_inicial')  # Redireciona para uma página de sucesso ou outra URL
     contexto = {
          'forms': form  # O nome correto seria 'form' e não 'forms'
     }

     return render(request, 'hospital/tela_form.html', contexto)
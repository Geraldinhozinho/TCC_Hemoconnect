from django.shortcuts import render,redirect
from .forms import UsuarioForm, QuestionarioForm
from .models import Usuario, Campanhas
from django.shortcuts import get_object_or_404
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
     form = UsuarioForm()
     if request.method == 'POST':
          form = UsuarioForm(request.POST)
          if form.is_valid():
               form.save()  # Salva o usuário no banco de dados
               return redirect('tela_inicial')  # Redireciona para uma página de sucesso ou outra URL
     contexto = {
          'form': form  # O nome correto seria 'form' e não 'forms'
     }

     return render(request, 'hospital/tela_login2.html', contexto)


#QUESTIONARIO 2 
def questionario(request):
    form = QuestionarioForm()
    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            print("Formulário é válido!")  # Verifica se a validação está correta
            form.save()  # Salva no banco de dados
            return redirect('tela_inicial')  # Redireciona após salvar
    contexto = {
        'form': form  # Certifique-se de que é 'form' e não 'forms'
    }
    return render(request, 'hospital/tela_form.html', contexto)



def campanhas(request):
    dados = Campanhas.objects.all()
    contexto = {
        'camp': dados
    }
    return render(request, 'hospital/campanhas.html', contexto)

def detalhe(request, id):
    campanha = get_object_or_404(Campanhas, id=id)  # Busca a campanha pelo ID ou retorna 404
    contexto = {
        'camp': campanha
    }
    return render(request, 'hospital/tela_detalhe_camp.html', contexto)


def perfil(request):
          
     return render(request, 'hospital/perfil.html')

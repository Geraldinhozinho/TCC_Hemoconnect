from django.shortcuts import render,redirect
from .forms import UsuarioForm, QuestionarioForm
from .models import Usuario, Campanhas
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
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
    campanhas = Campanhas.objects.all()  # Ou algum filtro específico
    context = {
        'campanhas': campanhas
    }
    return render(request, 'hospital/campanhas.html', context)

# def campanhas(request):
#     dados = Campanhas.objects.all()
#     dados_pag = Paginator(dados, 3)
#     page_num = request.GET.get('page')
#     page = dados_pag.get_page(page_num) 
#     contexto = {
#         'page': page
#     }
#     return render(request, 'hospital/campanhas.html', contexto)

from django.http import JsonResponse

def detalhe(request, campa_id):
    campanha = Campanhas.objects.get(id=campa_id)
    data = {
        "titulo": campanha.titulo,
        "descricao": campanha.descricao,
        "image_url": campanha.image.url,  # Corrigido para retornar o URL da imagem
    }
    return JsonResponse(data)
def doador(request):
          
     return render(request, 'hospital/tela_doador.html')

def contatos(request):
          
     return render(request, 'hospital/tela_contatos.html')

def perfil(request):
          
     return render(request, 'hospital/perfil.html')

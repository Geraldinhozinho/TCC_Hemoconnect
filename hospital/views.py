from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, QuestionarioForm
from .models import Campanhas, Questionario
from django.contrib import messages

# Create your views here.
# from django.shortcuts import get_object_or_404
# from django.core.paginator import Paginator
def inicio(request):
     return render(request, 'hospital/tela_inicial.html')



def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('tela_login2')  
        else:
            # Exibir mensagens de erro no template
            messages.error(request, "")
    else:
        form = UsuarioForm()
     
    return render(request, 'hospital/tela_login1.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        # Autenticar o usuário
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Loga o usuário
            return redirect('tela_inicial')  # Redireciona após login
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'hospital/tela_login2.html')

def logout_view(request):
    logout(request) 
    return redirect('tela_login1')  



#QUESTIONARIO 2 
@login_required
def questionario(request):
    # Verifica se o usuário já respondeu ao questionário
    if Questionario.objects.filter(usuario=request.user).exists():
        # Se já respondeu, redireciona para a tela de sucesso
        return redirect('sucesso')
    
    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            # Salva o formulário, associando ao usuário logado
            questionario = form.save(commit=False)
            questionario.usuario = request.user
            questionario.save()
            return redirect('sucesso')  # Redireciona para a tela de sucesso após envio
        else:
            messages.error(request, "Houve um erro no envio do formulário. Verifique os dados.")
    else:
        form = QuestionarioForm()

    return render(request, 'hospital/tela_formulario.html', {'form': form})


def questionario_sus(request):
    # Aqui você deve buscar o último questionário do usuário logado (ou um específico, conforme o caso)
    questionario = Questionario.objects.filter(usuario=request.user).last()  # Último questionário criado

    return render(request, 'hospital/sucesso.html', {'questionario': questionario})

@login_required
def editar(request, id):
    # Busca o questionário específico do usuário logado
    questionario = get_object_or_404(Questionario, id=id, usuario=request.user)

    if request.method == 'POST':
        form = QuestionarioForm(request.POST, instance=questionario)
        if form.is_valid():
            form.save()
            return redirect('sucesso')  # Substitua pelo nome da view desejada
        else:
            messages.error(request, "Erro ao atualizar o questionário. Verifique os dados.")
    else:
        form = QuestionarioForm(instance=questionario)

    return render(request, 'hospital/tela_form.html', {'form': form})





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

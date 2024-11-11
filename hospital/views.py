from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .forms import UsuarioForm, QuestionarioForm
from .models import Campanhas
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
            messages.error(request, "Erro ao cadastrar usuário. Verifique os dados informados.")
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
def questionario(request):
    # Verifique se o usuário está autenticado
    if request.user.is_authenticated:
        # Preencher o formulário com os dados do usuário, caso ele esteja autenticado
        form = QuestionarioForm()

        if request.method == 'POST':
            form = QuestionarioForm(request.POST)

            if form.is_valid():
                print("Formulário é válido!")  # Verifica se a validação está correta
                form.save()  # Salva no banco de dados
                return redirect('tela_inicial')  # Redireciona após salvar

        # Passa o contexto com o formulário e o nome do usuário
        contexto = {
            'form': form,  # Certifique-se de que é 'form' e não 'forms'
            'user': request.user  # Adiciona o usuário para preencher automaticamente o nome
        }

        return render(request, 'hospital/tela_form.html', contexto)
    
    else:
        # Caso o usuário não esteja logado, redirecione para a página de login
        return redirect('login')






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

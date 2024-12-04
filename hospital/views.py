from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, QuestionarioForm, FotoPerfilForm
from .models import Campanhas, Questionario, Doacoes,Usuario, Criador, ChatFAQ
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.conf import settings
import os

#TELA INICIAL
def inicio(request):
    campanhas = Campanhas.objects.all().order_by('-data_campanha')
    contexto = {
        'campanhas': campanhas
    }
    return render(request, 'hospital/tela_inicial.html',contexto)

#CADASTRAR USUÁRIO
def cadastrar(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso! Você já pode fazer login.')
            return redirect('tela_login2')  
        else:
            messages.error(request, "")
    else:
        form = UsuarioForm()
    contexto={
        'form': form
        }
    return render(request, 'hospital/tela_login1.html', contexto )

#LOGAR
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  
            return redirect('tela_inicial') 
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'hospital/tela_login2.html')

#SAIR/LOGOUT
@login_required
def logout_view(request):
    logout(request) 
    return redirect('tela_login1')  

#QUESTIONARIO 2 - DOAÇÃO 
@login_required
def questionario(request):
    if Questionario.objects.filter(usuario=request.user).exists():
        return redirect('sucesso')
    if request.method == 'POST':
        form = QuestionarioForm(request.POST)
        if form.is_valid():
            questionario = form.save(commit=False)
            questionario.usuario = request.user
            questionario.save()
            return redirect('sucesso')
        else:
            messages.error(request, "Houve um erro no envio do formulário. Verifique os dados.")
    else:
        form = QuestionarioForm()
        
    contexto= {
        'form': form
        }
    return render(request, 'hospital/tela_formulario.html', contexto )

#MENSAGEM DE SUCESSO
@login_required
def questionario_sus(request):
    questionario = Questionario.objects.filter(usuario=request.user).last() 
    
    contexto = {
        'questionario': questionario
        }
    
    return render(request, 'hospital/sucesso.html', contexto )

#QUESTIONARIO RESPONDIDO - EDITAR
@login_required  
def editar(request, id):
    questionario = get_object_or_404(Questionario, id=id, usuario=request.user)
    if request.method == 'POST':
        form = QuestionarioForm(request.POST, instance=questionario)
        if form.is_valid():
            form.save()
            return redirect('sucesso') 
        else:
            messages.error(request, "Erro ao atualizar o questionário. Verifique os dados.")
    else:
        form = QuestionarioForm(instance=questionario)

    contexto= {
        'form': form
        }
    
    return render(request, 'hospital/tela_formulario.html', contexto)

#CADASTRAR E REMOVER CAMPANHAS - APENAS O ADMIN
def campanhas(request):
    campanhas = Campanhas.objects.all().order_by('-data_campanha')
    contexto = {
        'campanhas': campanhas
    }
    return render(request, 'hospital/campanhas.html', contexto)

#DETALHAR CAMPANHAS
def detalhe(request, campa_id):
    campanha = Campanhas.objects.get(id=campa_id)
    contexto = {
        "titulo": campanha.titulo,
        "descricao": campanha.descricao,
        "image_url": campanha.image.url,  
    }
    return JsonResponse(contexto)

#TELA DO DOADOR
def doador(request):     
     return render(request, 'hospital/tela_doador.html')

#TELA DE CONTATOS
def contatos(request):
    listar = ChatFAQ.objects.all()
    contexto ={
        'lista': listar
    }
    return render(request, 'hospital/tela_contatos.html',contexto )

#TELA DE PERFIL
@login_required
def perfil(request):   
    user = request.user  
    try:
        questionario = Questionario.objects.get(usuario=user)
    except Questionario.DoesNotExist:
        questionario = None  

    doacoes = user.doacoes.order_by('-data_doacao')   # Recupere as doações do usuário logado

    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('tela_perfil')  
    else:
        form = FotoPerfilForm(instance=user)
    
    contexto= {
        'form': form,
        'user': user,
        'questionario': questionario,
        'doacoes': doacoes  
    }
    
    return render(request, 'hospital/tela_perfil.html', contexto)

#DELETAR FOTO DO USUÁRIO
@login_required
def deletar_foto(request):
    user = request.user 
    if user.foto_perfil: 
        caminho_foto = os.path.join(settings.MEDIA_ROOT, str(user.foto_perfil))
        if os.path.exists(caminho_foto):
            os.remove(caminho_foto)
        user.foto_perfil = None
        user.save()
    return redirect('tela_perfil')

#TELAS DOS CRIADORES
def criadores(request):
    criadores = Criador.objects.all()  
    paginator = Paginator(criadores, 2)  # 2 criadores por página
    
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 
     
    contexto={
        'pagina': page_obj
        }
    return render(request, 'hospital/tela_criadores.html',contexto )





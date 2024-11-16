from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, QuestionarioForm, FotoPerfilForm
from .models import Campanhas, Questionario
from django.contrib import messages
from django.http import JsonResponse


def inicio(request):
     return render(request, 'hospital/tela_inicial.html')

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
     
    return render(request, 'hospital/tela_login1.html', {'form': form})

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

#SAIR
def logout_view(request):
    logout(request) 
    return redirect('tela_login1')  



#QUESTIONARIO 2 
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
    return render(request, 'hospital/tela_formulario.html', {'form': form})

#MENSAGEM DE SUCESSO
def questionario_sus(request):
    questionario = Questionario.objects.filter(usuario=request.user).last() 
    return render(request, 'hospital/sucesso.html', {'questionario': questionario})

#QUESTIONARIO EDITAR  
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

    return render(request, 'hospital/tela_formulario.html', {'form': form})


def campanhas(request):
    campanhas = Campanhas.objects.all() 
    context = {
        'campanhas': campanhas
    }
    return render(request, 'hospital/campanhas.html', context)

def detalhe(request, campa_id):
    campanha = Campanhas.objects.get(id=campa_id)
    data = {
        "titulo": campanha.titulo,
        "descricao": campanha.descricao,
        "image_url": campanha.image.url,  
    }
    return JsonResponse(data)

def doador(request):
          
     return render(request, 'hospital/tela_doador.html')

def contatos(request):
          
     return render(request, 'hospital/tela_contatos.html')

@login_required
def perfil(request):
    user = request.user  # Usuário logado

    # Buscando o questionário associado ao usuário logado
    try:
        questionario = Questionario.objects.get(usuario=user)
    except Questionario.DoesNotExist:
        questionario = None  # Caso o questionário não exista para o usuário

    if request.method == 'POST':
        form = FotoPerfilForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('tela_perfil')  # Redireciona após salvar
    else:
        form = FotoPerfilForm(instance=user)
    
    return render(request, 'hospital/tela_perfil.html', {
        'form': form,
        'user': user,
        'questionario': questionario  # Passa o questionário para o template
    })


import os

from django.conf import settings
import os


def deletar_foto(request):
    user = request.user
    if user.foto_perfil:  # Verifica se existe uma foto
        # Remove a foto do sistema de arquivos
        caminho_foto = os.path.join(settings.MEDIA_ROOT, str(user.foto_perfil))
        if os.path.exists(caminho_foto):
            os.remove(caminho_foto)

        # Remove a foto do banco de dados
        user.foto_perfil = None
        user.save()
    return redirect('tela_perfil')

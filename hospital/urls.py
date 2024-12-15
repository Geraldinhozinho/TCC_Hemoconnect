from django.urls import path
from hospital.views import cadastrar, login_view, inicio, doador, campanhas,  detalhe,  contatos, perfil, logout_view, deletar_foto, questionario , questionario_sus, editar,criadores, get_faq
urlpatterns = [
    
    #TELAS DE LOGIN E CADASTRO
    path('cadastrar/', cadastrar, name='tela_login1'),
    path('logar/', login_view, name='tela_login2'),
    
    #TELAS PRINCIPAIS
    path('',inicio, name='tela_inicial'), #TELA INICIAL
    path('doador/',doador, name='tela_doador'), #TELA DO DOADOR
    path('campanhas/', campanhas, name='campanhas'), #TELA DE CAMPANHAS
    path('tela_detalhe_camp/<int:campa_id>/', detalhe, name='tela_detalhe_camp'), #TELA DE DETALHAR AS CAMPANHAS
    path('contatos/',contatos, name='tela_contatos'), #TELA DE CONTATOS
    path('perfil/', perfil, name='tela_perfil'), #TELA DO PERFIL
    path('logout/', logout_view, name='logout'), #SAIR DO PERFIL
    path('deletar-foto/', deletar_foto, name='deletar_foto'), #DELETAR FOTO DO PERFIL
    
    #TELA DE REDIRECIONAMENTO
    path('quest', questionario, name='tela_form'), #TELA DO QUESTIONARIO
    path('sucesso/', questionario_sus, name='sucesso'), #TELA APÓS O QUESTIONÁRIO SER RESPONDIDO
    path('questionario/editar/<int:id>/', editar, name='editar_questionario'), #TELA APÓS O QUESTIONÁRIO SER RESPONDIDO E QUISER EDITAR
    path('api/faqs/', get_faq, name='get_faq'),
   #TELA DOS COLABORADORES
    path('Criadores/', criadores, name='tela_criadores'),
]

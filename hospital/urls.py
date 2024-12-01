from django.urls import path
from hospital.views import inicio, cadastrar, login_view, questionario,perfil, campanhas, detalhe, doador, contatos, logout_view, editar,questionario_sus,deletar_foto, criadores
urlpatterns = [
    
    path('',inicio, name='tela_inicial'),
    
    path('campanhas/', campanhas, name='campanhas'),
    path('tela_detalhe_camp/<int:campa_id>/', detalhe, name='tela_detalhe_camp'),
    
    path('doador/',doador, name='tela_doador'),
    path('quest', questionario, name='tela_form'),
    path('sucesso/', questionario_sus, name='sucesso'),
    path('questionario/editar/<int:id>/', editar, name='editar_questionario'),
   

    
    path('contatos/',contatos, name='tela_contatos'),
    
    path('cadastrar/', cadastrar, name='tela_login1'),
    path('logar/', login_view, name='tela_login2'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil, name='tela_perfil'),
    path('deletar-foto/', deletar_foto, name='deletar_foto'),
    
    
    
    path('Criadores/', criadores, name='tela_criadores'),
]

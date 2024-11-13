"""
URL configuration for hemoconnect project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital.views import inicio, cadastrar, login_view, questionario,perfil, campanhas, detalhe, doador, contatos, logout_view, editar,questionario_sus
from django.conf import settings
from django.conf.urls.static import static
app_name = 'hospital'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='tela_inicial'),
    
    path('campanhas/', campanhas, name='campanhas'),
    path('tela_detalhe_camp/<int:campa_id>/', detalhe, name='tela_detalhe_camp'),
    
    path('doador/',doador, name='tela_doador'),
    path('quest/', questionario, name='tela_form'),
    path('sucesso/', questionario_sus, name='sucesso'),
    path('questionario/editar/<int:id>/', editar, name='editar_questionario'),
    
    
    path('contatos/',contatos, name='tela_contatos'),
    
    
    path('cadastrar/', cadastrar, name='tela_login1'),
    path('logar/', login_view, name='tela_login2'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil, name='perfil')
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
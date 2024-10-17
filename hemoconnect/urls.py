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
from hospital.views import inicio, cadastro, login, questionario,perfil, campanhas, detalhe, doador, contatos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio, name='tela_inicial'),
    path('cadastrar/', cadastro, name='tela_login1'),
    path('logar/', login, name='tela_login2'),
    path('quest/', questionario, name='tela_form'),
    path('perfil/', perfil, name='perfil'),
    path('campanhas/', campanhas, name='campanhas'),
    path('campanhas/<int:id>/',detalhe, name='tela_detalhe_camp'),
    path('doador/',doador, name='tela_doador'),
    path('contatos/',contatos, name='tela_contatos'),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
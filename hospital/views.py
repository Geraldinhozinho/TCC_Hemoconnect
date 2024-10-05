from django.shortcuts import render

# Create your views here.

def login1(request):
     return render(request, 'hospital/tela_login1.html')
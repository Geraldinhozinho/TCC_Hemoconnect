from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):
    nome_completo =models.CharField(max_length=200, default='')
    cpf = models.CharField(max_length=11, unique=True, verbose_name="CPF")
    endereco = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.username

    

class Questionario(models.Model):
    
    CHOICES = [
        ('sim', 'Sim'),
        ('nao', 'Não'),
    ]
    
    TIPOS_SANGUINEOS = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('Não sei', 'Não sei'),
    ]
    DIAS_SEMANA = [
        ('seg', 'Segunda'),
        ('ter', 'Terça'),
        ('qua', 'Quarta'),
        ('qui', 'Quinta'),
        ('sex', 'Sexta'),
        ('sab', 'Sábado'),
        ('dom', 'Domingo'),
    ]
     
    querer = models.CharField(
        max_length=5,
        choices=CHOICES,
        default=True 
    )

    nome = models.CharField(max_length=150)
    email = models.EmailField() 
       
    tipo_sangue = models.CharField(max_length=10,
        choices=TIPOS_SANGUINEOS,
        default=True 
    )
    
    fuma = models.CharField(
        max_length=3,
        choices=CHOICES,
        default=True
    )
    
    sexo = models.CharField(
        max_length=9,
        choices=CHOICES,
        default=True
    )
    doenca = models.CharField(
        max_length=3,
        choices=CHOICES,
        default=True
    )
    doenca_det = models.CharField(
        max_length=150,
        blank=True, null=True)  
    
    disponibilidade = models.CharField(
        max_length=3,
        choices=CHOICES,
        default=True)
    
    dias = MultiSelectField(
        max_length=15,
        choices=DIAS_SEMANA,
        default=True,
        null=False
        )

    def __str__(self):
        return self.nome
    

class Campanhas(models.Model):
    titulo = models.CharField(max_length=20, null=True, blank=True)
    descricao = models.TextField(null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
  
    def __str__(self):
        return self.titulo
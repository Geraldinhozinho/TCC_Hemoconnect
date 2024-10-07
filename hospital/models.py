from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    senha = models.CharField(max_length=10)
    confir = models.CharField(max_length=10)
    
    def __str__ (self):
        return self.nome
    

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
    
    dias = models.CharField(
        max_length=15,
        choices=DIAS_SEMANA,
        default=True)

    def __str__(self):
        return self.nome
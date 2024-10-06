from django.db import models

# Create your models here.


class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField()
    senha = models.CharField(max_length=10)
    confir = models.CharField(max_length=10)
    
    def __str__ (self):
        return self.nome
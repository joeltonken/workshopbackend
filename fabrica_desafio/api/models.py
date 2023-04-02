from django.db import models
import uuid

# Create your models here.

def upload_imagem_filme(instance, filename):
    return f"{instance.id}-{filename}"

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    ano = models.IntegerField()
    diretor = models.CharField(max_length=155)
    imagem_filme = models.ImageField(upload_to=upload_imagem_filme, blank=False, null=True)
    data_cadastro = models.DateField(auto_now_add=True, null= True, blank=False)
        
    DISPONIBILIDADE_CHOICES = [
    ('netflix', 'Netflix'), ('cinema', 'Cinema'), ('hbo', 'HBO'),
    ('appletv', 'AppleTV'), ('prime_video', 'Prime Vídeo'), ('globoplay', 'Globoplay'), ('disney', 'Disney+'), ('outros', 'Outros'),
  ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False, editable=False)
    
    disponibilidade = models.CharField(max_length=25, null=False, blank=False,
    choices=DISPONIBILIDADE_CHOICES)
    
    def __str__(self):
        return self.titulo
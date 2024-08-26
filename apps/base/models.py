from django.db import models

class Categoria(models.Model):
    nome = models.CharField("Nome", max_length=50)
    slug = models.SlugField("Slug", max_length=50)
    
    
    def __str__(self) -> str:
        return self.nome

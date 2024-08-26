from django.db import models
from apps.base.models import Categoria


class Empresa(models.Model):
    nome = models.CharField("Nome", max_length=200)
    slug = models.SlugField("Slug", max_length=50)
    documento = models.CharField("Documento", max_length=35, null=True, blank=True)
    endereco = models.CharField("endereço", max_length=200)
    telefone = models.CharField("Telefone", max_length=35)
    email = models.EmailField("e-mail", null=True, blank=True)
    facebook = models.URLField('Facebook', null=True, blank=True)
    instagram = models.URLField('Instagram', null=True, blank=True)
    youtube = models.URLField('Youtube', null=True, blank=True)
    xtwitter = models.URLField('Xtwitter', null=True, blank=True)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    def __str__(self):
        return self.nome
    

# Slider.

class Slider(models.Model):
    titulo = models.CharField("Titulo", max_length=200)
    slug = models.SlugField("Slug", max_length=50)
    descricao = models.TextField("Descrição")
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE,
        related_name="cat_slide",
        verbose_name="Categoria" 
        )
    imagem = models.ImageField("Imagem", upload_to="slider")
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)
    
    def __str__(self):
        return self.titulo

# About

class About(models.Model):
     titulo = models.CharField("Titulo", max_length=200)
     slug = models.SlugField("Slug", max_length=50)
     descricao = models.TextField("Descrição")
     descricao_dois = models.TextField("Descrição Dois", null=True, blank=True)
     descricao_tres = models.TextField("Descrição Três", null=True, blank=True)
     created = models.DateTimeField('Criado em', auto_now_add=True)
     modified = models.DateTimeField('Modificado em', auto_now=True)
     
     def __str__(self):
        return self.titulo
    

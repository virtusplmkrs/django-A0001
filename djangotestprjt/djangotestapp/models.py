from django.db import models
from django.contrib.auth.models import User

#usando Tuplas para valores de Status
STATUS = (
  (0,"Draft"),
  (1, "Publish")
)

class Post(models.Model):
  title = models.CharField(max_length=200, unique=True, verbose_name='Titulo')
  slug = models.CharField(max_length=200, unique=True)
  author = models.ForeignKey(User, on_delete = models.CASCADE, related_name='blog_posts', verbose_name='Author')
  updated_on = models.DateTimeField(auto_now = True, verbose_name='Dt. Atualização')
  sumary = models.TextField(max_length=300, verbose_name='Resumo')
  content = models.TextField(verbose_name='Postagem')
  created_on = models.DateTimeField(auto_now_add=True, verbose_name='Dt. Criação')
  status = models.IntegerField(choices=STATUS, default=0, verbose_name='Status')
  
  class Meta:
    ordering = ['-created_on']
    
  def __str__(self):
    return self.title
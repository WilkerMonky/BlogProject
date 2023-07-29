from django.db import models
from stdimage import StdImageField
import uuid
from django.utils.text import slugify
from django.contrib.auth.models import User



def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename
 

class BaseModel(models.Model):
    criacao = models.DateField('Criação', auto_now_add=True)
    edicao = models.DateField('Edição', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    class Meta:
        abstract = True  


class PostModel(BaseModel):
 
    titulo = models.CharField('Título', max_length=200)
    subtitulo = models.CharField('SubTítulo', max_length=300)
    conteudo = models.TextField('Conteúdo')
    resumo = models.CharField('Resumo', max_length=300)
    link = models.CharField('Link', max_length=300)
    miniatura = StdImageField(upload_to= get_file_path, variations={'thumbnail':{'width':374, 'height':260, 'crop':True}})
    capaPagina = StdImageField(upload_to=get_file_path, variations={'thumbnail':{'width':1200,'height':444, 'crop':True}})
    slug = models.SlugField(unique=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo
    

class TopicoModel(BaseModel):
    nome = models.CharField('Nome', max_length=100)
    miniatura = StdImageField(upload_to=get_file_path, variations={'thumbnail':{'width':250,'height':200}})
    slug = models.SlugField(unique=True, blank=True)
    subtitulo = models.CharField('Subtítulo', max_length=300)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nome)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Tópico'
        verbose_name_plural = 'Tópicos'

    def __str__(self):
        return self.nome


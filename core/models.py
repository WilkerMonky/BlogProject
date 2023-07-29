from django.db import models
from stdimage import StdImageField
import uuid
from django.utils.text import slugify


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    
    return filename


class BaseModel(models.Model):
    criacao = models.DateTimeField('Criação', auto_now_add=True)
    edicao = models.DateTimeField('Edição', auto_now=True)
    ativo = models.BooleanField('Ativo', default=True)
    class Meta:
        abstract = True


class PostModel(BaseModel):
    titulo = models.CharField('Título', max_length=200)
    resumo = models.CharField('Resumo', max_length=300)
    link = models.CharField('Link', max_length=300)
    miniatura = StdImageField(upload_to= get_file_path, variations={'thumbnail':{'width':374, 'height':260, 'crop':True}})
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = 'Post Curiosidade'
        verbose_name_plural = 'Posts Curiosidades'

    def __str__(self):
        return self.titulo

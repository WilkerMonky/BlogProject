from django.contrib import admin
from .models import PostModel, TopicoModel

@admin.register(PostModel)
class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criacao','ativo')
    exclude = ('slug',)


@admin.register(TopicoModel)
class TopicoAdmin(admin.ModelAdmin):
    list_display=('nome', 'criacao', 'ativo')
    exclude = ('slug',)
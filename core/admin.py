from django.contrib import admin
from .models import PostModel

@admin.register(PostModel)
class PostCuriosidadeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'criacao','ativo')
    exclude = ('slug',)
from typing import Any, Dict
from django.views.generic import TemplateView
from .models import PostModel


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['postsC'] = PostModel.objects.all()
        
        return context
    
class MateriaView(TemplateView):
    template_name = 'materia.html'
    
    def get_context_data(self, **kwargs):
        context =  super(MateriaView, self).get_context_data(**kwargs)
        slug = kwargs['slug']
        context['postC'] = PostModel.objects.get(slug=slug)
           
        return context

    

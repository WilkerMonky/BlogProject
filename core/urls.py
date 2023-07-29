from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import DetailView
from .views import IndexView, MateriaView
from .models import PostModel # Certifique-se de importar o modelo correto

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('materia/<slug:slug>/', MateriaView.as_view(template_name='materia.html'), name='materia'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

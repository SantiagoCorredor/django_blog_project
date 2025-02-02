from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView
)

from .models import Entry, Category

class Entrylistview(ListView):
    template_name = "entrada/lista.html"
    context_object_name = 'entradas'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(Entrylistview, self).get_context_data(**kwargs)
        context ["categorias"] = Category.objects.all()

        return context 

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '')   

        resultado = Entry.objects.buscar_entrada(kword, categoria)

        return resultado
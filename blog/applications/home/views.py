import datetime
#
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

from django.views.generic import (
    TemplateView,
    CreateView
)
from applications.entrada.models import Entry
from .models import home
from .forms import SuscriberForm

class HomePageView(TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs ):
        content = super(HomePageView, self).get_context_data(**kwargs)  
        #cargar home
        content["home"] = home.objects.latest('created')
        #cargar portada
        content["portada"] = Entry.objects.entrada_en_portada()
        # contexto para los demas articulos en home
        content["entradas_home"] = Entry.objects.entradas_en_home()
        # contexto para los demas ariticulos recientes
        content["entradas_recientes"] = Entry.objects.entradas_recientes()
        #envio de formulario
        content["form"] = SuscriberForm
        return content

class SuscriberCreateView(CreateView):
    form_class = SuscriberForm
    success_url = '.'
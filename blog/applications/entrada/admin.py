from django.contrib import admin
from .models import Category, Tag, Entry  # Importa los modelos

# Registra los modelos en el administrador
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Entry)

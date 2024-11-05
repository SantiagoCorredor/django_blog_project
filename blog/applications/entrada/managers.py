from django.db import models

class EntryManager(models.Manager):

    def entrada_en_portada(self):
        return self.filter(
            public = True,
            portada = True,
        ).order_by('-created').first()
    
    def entradas_en_home(self):
        return self.filter(
            public = True,
            in_come = True
        ).order_by('-created')[:4]
    
    def entradas_recientes(self):
        return self.filter(
            public = True,
        ).order_by('-created')[:3]
    def buscar_entrada(self, kword, categoria):
        if len(categoria) > 0:
            return self.fiter(
                category__short_name = categoria,
                title__icontains = kword,
                public = True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains = kword,
                public = True
            ).order_by('-created')
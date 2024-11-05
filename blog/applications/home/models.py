from django.db import models

# Create your models here.

from model_utils.models import TimeStampedModel

class home (TimeStampedModel):
    title = models.CharField(
        'Nombre',
        max_length=30         
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros',
        max_length = 50
    )
    about_text = models.TextField()
    contact_email = models.TextField(
        'Email de contacto',
        blank = True,
        null = True
    )
    phone = models.CharField(
        'Telefono de contacto',
        max_length=20
    )
    class Meta:
        verbose_name = 'Pagina principal'
        verbose_name_plural = 'Pagina principal'
    def __str__(self):
        return self.title
    
class Suscriber(TimeStampedModel):
    email = models.EmailField()
    class Meta: 
        verbose_name = 'Suscriptor'
        verbose_name_plural = 'Suscriptores'
    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    full_name = models.CharField(
        'Nombres',
        max_length=60
    )
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__ (self):
        return self.full_name
from django import forms

from .models import Suscriber

class SuscriberForm(forms.ModelForm):
    class Meta:
        model = Suscriber
        fields = (
            'email',
        )
        widgets = {
            'email': forms.EmailInput(
                attrs= {
                    'placeholder' : 'correo electronico...'
                }
            )

        }
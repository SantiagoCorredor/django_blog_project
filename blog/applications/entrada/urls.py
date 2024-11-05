#
from django.urls import path
from . import views

app_name = "entrada_app"

urlpatterns = [
    path(
        'entradas',
        views.Entrylistview.as_view(),
        name = 'entry-lista',
    )
]
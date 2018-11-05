from django.urls import path
from django.views.generic import TemplateView

from pesquisa_alter.core import views as v

app_name = 'core'

urlpatterns = [
    path('', v.index, name='index'),
    path('person/json/', v.person_json, name='person_json'),
    path(
        'pesquisa/',
        TemplateView.as_view(template_name='add_pesquisa.html'),
        name='add_pesquisa'
    ),
]

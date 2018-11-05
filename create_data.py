import os
import django
import timeit

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pesquisa_alter.settings")
django.setup()

# from django.utils.text import slugify
from pesquisa_alter.core.models import Questions

tic = timeit.default_timer()


QUESTIONS = (
    'Qual o nível de receptividade do sistema?',
    'Qual o nível de implementação?',
    'Qual o nível de implantação?',
    'Existem algum controle manual?',
)

aux = []
for question in QUESTIONS:
    obj = Questions(question=question)
    aux.append(obj)

Questions.objects.bulk_create(aux)

toc = timeit.default_timer()
print('time', toc - tic)

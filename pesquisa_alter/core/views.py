from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from .models import Person, Questions, Pesquisa
from .forms import PesquisaForm


def index(request):
    context = {}
    person_list = Person.objects.all()
    context['person_list'] = person_list
    return render(request, 'index.html', context)


def person_detail(request, pk):
    context = {}
    person = get_object_or_404(Person, pk=pk)
    context['person'] = person
    # Retornando todas as pesquisas de uma pessoa.
    pesquisas = Pesquisa.objects.filter(person=person)
    context['pesquisas'] = pesquisas
    return render(request, 'person_detail.html', context)


def person_json(request):
    persons = Person.objects.all()
    data = [person.to_dict_json() for person in persons]
    response = {'data': data}
    return JsonResponse(response)


def pesquisa_add(request):
    template_name = 'pesquisa_add.html'
    if request.method == 'POST':
        form = PesquisaForm(request.POST)
        if form.is_valid():
            data = dict(
                search_key=form.cleaned_data['search_key'],
                person=form.cleaned_data['person'],
                researched=form.cleaned_data['researched'],
                questions=Questions.objects.all(),
            )
            criar_pesquisa(**data)
            # Não usar o método save().
            # form.save()
            return redirect('core:index')
    else:
        form = PesquisaForm()
    context = {'form': form}
    return render(request, template_name, context)


def criar_pesquisa(**data):
    # Pegando somente as perguntas
    questions = data['questions']
    pesquisas = []
    for question in questions:
        obj = Pesquisa(
            search_key=data['search_key'],
            person=data['person'],
            researched=data['researched'],
            question=question
        )
        pesquisas.append(obj)
    Pesquisa.objects.bulk_create(pesquisas)

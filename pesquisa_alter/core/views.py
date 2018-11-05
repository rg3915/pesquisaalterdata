from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import Person, Questions, Pesquisa


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


def add_pesquisa(request):
    # context = {}
    # person_list = Person.objects.all()
    # context['person_list'] = person_list
    return render(request, 'add_pesquisa.html')


def person_create(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)

        if form.is_valid():
            print('<<<<==== FORM VALIDO ====>>>>')
            new = form.save(commit=False)
            new.save()
            form.save_m2m()

            return HttpResponseRedirect('/cliente/lista/')
        else:
            print('<<<<==== AVISO DE FORMULARIO INVALIDO ====>>>>')
            print(form)
            return render(request, 'person_create.html', {'form': form})
    else:
        context = {'form': PersonForm()}
        return render(request, 'person_create.html', context)


def addAllQuestionsInPesquisa(request):
    person = Person.objects.get(pk=1)
    questions = Questions.objects.all()

    for question in questions:
        try:
            Pesquisa.objects.get(
                search_key='092018',
                person=person,
                question=question
            )
            print('existe')
        except Pesquisa.DoesNotExist:
            Pesquisa.objects.get_or_create(
                search_key='092018',
                person=person,
                question=question,
                response='I'
            )
            print('Não existe')

    return HttpResponseRedirect('bolsa/pesquisa/listar')

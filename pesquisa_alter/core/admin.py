from django.contrib import admin
from .models import Person, Questions, Pesquisa


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'email', 'phone', 'cdalterdata')
    search_fields = ('cdalterdata', 'name', 'email')
    #list_filter = ('gender',)


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('__str__', )


@admin.register(Pesquisa)
class PesquisaAdmin(admin.ModelAdmin):
    list_display = ('__str__', )

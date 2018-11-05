from django.db import models
from django.urls import reverse
from django.utils import timezone


class Person(models.Model):
    cdalterdata = models.IntegerField('Cód. Alterdata')
    name = models.CharField('nome', max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField('telefone', max_length=11, null=True, blank=True)
    # GENDER = (
    #     ('0', ''),
    #     ('man', 'homem'),
    #     ('woman', 'mulher'),
    # )
    # gender = models.CharField(
    #     'sexo',
    #     max_length=5,
    #     choices=GENDER,
    #     default='0'
    # )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.name

    def to_dict_json(self):
        return {
            'cdalterdata': self.cdalterdata,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            # 'gender': self.get_gender_display(),
        }

    def get_absolute_url(self):
        return reverse('pesquisa_alter:add_pesquisa', args=[str(self.id)])


class Questions(models.Model):
    LEVEL_CHOICES = (
        ('0', 'Indefinido'),
        ('1', 'Dependencia'),
        ('2', 'Confianca'),
        ('3', 'Comprometimento'),
        ('4', 'Preditiva'),
        ('5', 'Comprometimento'),
    )
    question = models.CharField('Pergunta', max_length=200)
    level = models.CharField('Nível', max_length=15,
                             choices=LEVEL_CHOICES, default='0')

    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ('-level',)

    def __str__(self):
        return self.question


class PesquisaManager(models.Manager):

    def add_question(self, search_key, question):
        pesquisa, created = self.get_or_create(
            search_key=search_key, question=question)
        if not created:
            pesquisa.person = pesquisa.person
            pesquisa.question = pesquisa.question
            pesquisa.save()
        return pesquisa


class Pesquisa(models.Model):
    RESPOSTA_CHOICES = (
        ('V', 'Verdadeiro'),
        ('F', 'Falso'),
        ('I', 'Indefinido'),
    )
    search_key = models.CharField(
        'Chave da pesquisa', max_length=200, db_index=False)
    person = models.ForeignKey(
        'core.person', related_name='Pessoa', on_delete=models.CASCADE)
    researched = models.CharField('Entrevistado', max_length=200)
    question = models.ForeignKey(
        'core.Questions', related_name='Pergunta', on_delete=models.CASCADE,)
    response = models.CharField(
        'Resposta', max_length=1, choices=RESPOSTA_CHOICES, default='I')
    # participation_on = models.DateField('período da pesquisa', default=timezone.now)
    participation_on = models.DateField(
        'período da pesquisa',
        auto_now_add=True,
        auto_now=False
    )
    created_on = models.DateTimeField(
        'solicitado em',
        auto_now_add=True,
        auto_now=False
    )

    objects = PesquisaManager()

    class Meta:
        verbose_name = 'Pesquisa'
        verbose_name_plural = 'Pesquisas'
        unique_together = (('search_key', 'person', 'question'),)
        ordering = ('-participation_on',)

    def __str__(self):
        return self.question.question

    # def get_absolute_url(self):
    #     return reverse('scheduling:agendamento')

# from django import forms
#
# from django.contrib.admin.widgets import AdminTextInputWidget, FilteredSelectMultiple
# from django.utils import timezone
#
# from pesquisa_alter.core.models import Pesquisa, Person
#
# RESPOSTA_CHOICES = (
#     ('V', 'Verdadeiro'),
#     ('F', 'Falso'),
#     ('I', 'Indefinido'),
# )
#
# class PesquisaForm(forms.ModelForm):
#     search_key = forms.CharField('Chave da pesquisa', max_length=200, db_index=False)
#     person = forms.ModelChoiceField(label='Cliente', widget=forms.Select(attrs={'class': 'form-control'}), required=True, queryset=Person.objects.all())
#     researched = forms.CharField('Entrevistado', max_length=200, db_index=False)
#     question = forms.CharField('Pergunta')
#     response = forms.ChoiceField(label='Resposta',  widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=RESPOSTA_CHOICES, default='I')
#     participation_on = forms.DecimalField('período dapesquisa', default=timezone.now)
#     created_on = forms.DecimalField('solicitado em', default=timezone.now)
#     #
#     #
#     # person = forms.ModelChoiceField(label='Pessoa', widget=forms.Select(attrs={'class': 'form-control'}), required=True, queryset=Person.objects.all())
#     # transaction_kind = forms.ChoiceField(label='Tipo Movimento', widget=forms.Select(attrs={'class': 'form-control'}), required=True, choices=TRANSACTION_KIND)
#     # value_moved = forms.DecimalField(label='Valor Movimentado', widget=AdminTextInputWidget(attrs={'class': 'form-control input-lg'}) , max_digits=10, decimal_places=2)
#     # date_return = forms.DateField(label='Dt. Retorno', widget=forms.TextInput(attrs={'class': 'form-control input-lg'}))
#
#     # def __init__(self, *args, **kwargs):
#     #     super(PesquisaForm, self).__init__(*args, **kwargs)
#     #     self.fields['value_moved'].localize = True
#     #     self.fields['value_moved'].widget.is_localized = True
#
#     class Meta:
#         model = Pesquisa
#         exclude = ['created_on','participation_on']
#         fields = '__all__'
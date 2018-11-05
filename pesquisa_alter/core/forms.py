from django import forms
from pesquisa_alter.core.models import Pesquisa


class PesquisaForm(forms.ModelForm):
    # person = forms.ModelChoiceField(label='Cliente', widget=forms.Select(
    #     attrs={'class': 'form-control'}), required=True, queryset=Person.objects.all())
    # response = forms.ChoiceField(label='Resposta',  widget=forms.Select(
    # attrs={'class': 'form-control'}), required=True,
    # choices=RESPOSTA_CHOICES)

    class Meta:
        model = Pesquisa
        fields = (
            'search_key',
            'person',
            'researched',
        )

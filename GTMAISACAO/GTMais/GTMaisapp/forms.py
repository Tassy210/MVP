from django import forms
from .models import AcaoExtensao, Cidades, Estados
class AcaoExtensaoForm(forms.ModelForm):
    idEstado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        widget=forms.Select(attrs={'id': 'estado'})
    )
    idCidade = forms.ModelChoiceField(
        queryset=Cidades.objects.none(),
        widget=forms.Select(attrs={'id': 'cidade'})
    )
    def clean(self):
        cleaned_data = super().clean()
        id_estado = cleaned_data.get('idEstado')
        id_cidade = cleaned_data.get('idCidade')

        if id_estado and id_cidade:
            if not Cidades.objects.filter(idCidade=id_cidade, UF=id_estado).exists():
                raise forms.ValidationError("A cidade selecionada não corresponde ao estado.")

        return cleaned_data
    class Meta:
        model = AcaoExtensao
        fields = [
            'TituloAcao',
            'coordenadorAcao',
            'alunoAcao',
            'descricao',
            'idTipo',
            'idSituacao',
            'dtCriacao',
            'dtModificacao',
            'dtInicio',
            'dtFim',
            'CEP',
            'idEstado',
            'idCidade',
            'Numero',
            'Complemento',
            'Bairro',
            'Rua',
        ]

        widgets = {
            'dtCriacao': forms.DateInput(attrs={'type': 'date'}),
            'dtModificacao': forms.DateInput(attrs={'type': 'date'}),
            'dtInicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dtFim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control', 'id': 'cep'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control', 'id': 'bairro'}),
            'Rua': forms.TextInput(attrs={'class': 'form-control', 'id': 'rua'}),
            'idEstado': forms.Select(attrs={'class': 'form-control', 'id': 'estado'}),
            'idCidade': forms.Select(attrs={'class': 'form-control', 'id': 'cidade'}),
        }
    def clean(self):
        cleaned_data = super().clean()
        id_estado = cleaned_data.get('idEstado')
        id_cidade = cleaned_data.get('idCidade')

        if id_estado and id_cidade:
            # Verifica se a cidade pertence ao estado selecionado
            if not Cidades.objects.filter(idCidade=id_cidade, UF=id_estado).exists():
                raise forms.ValidationError("A cidade selecionada não corresponde ao estado.")

        return cleaned_data
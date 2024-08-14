from django import forms
from .models import AcaoExtensao, Cidades, Estados, ContatoAcao, EdicaoAcao, Endereco

class ContatoForm(forms.ModelForm):
    class Meta:
        model = ContatoAcao
        fields = ['nome', 'telefone', 'email', 'titulo', 'descricao']
        widgets = {
            'descricao': forms.Textarea(attrs={'class': 'form-group', 'id': 'descricao', 'name': 'descricao'}),
        }
class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = [
            'CEP',
            'numero',
            'complemento',
            'rua',
            'bairro',
        ]
        widgets = {
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'numero': forms.NumberInput(attrs={'class': 'form-control'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control'}),
            'rua': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
        }
from django import forms
from .models import AcaoExtensao, Endereco, EdicaoAcao

class AcaoExtensaoForm(forms.ModelForm):
    endereco_CEP = forms.CharField(label='CEP', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_numero = forms.IntegerField(label='Número', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    endereco_complemento = forms.CharField(label='Complemento', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_rua = forms.CharField(label='Rua', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco_bairro = forms.CharField(label='Bairro', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AcaoExtensao
        fields = [
            'TituloAcao',
            'coordenadorAcao',
            'alunoAcao',
            'descricao',
            'idTipo',
            'dtCriacao',
            'imagem',
            'contato',
            'artigo',
            'aceitaContribuicoes',      
            'idSituacao',
        
        ]
        widgets = {
            'dtCriacao': forms.DateInput(attrs={'type': 'date'})
        }

    def save(self, commit=True):
        acao_extensao = super().save(commit=False)

        endereco = Endereco(
            CEP=self.cleaned_data['endereco_CEP'],
            numero=self.cleaned_data['endereco_numero'],
            complemento=self.cleaned_data['endereco_complemento'],
            rua=self.cleaned_data['endereco_rua'],
            bairro=self.cleaned_data['endereco_bairro']
        )
        if commit:
            endereco.save()
            acao_extensao.idEndereco = endereco
            acao_extensao.save()

        return acao_extensao

class EdicaoAcaoForm(forms.ModelForm):
    idEstado = forms.ModelChoiceField(
        queryset=Estados.objects.all(),
        widget=forms.Select(attrs={'id': 'estado'})
    )
    idCidade = forms.ModelChoiceField(
        queryset=Cidades.objects.none(),  
        widget=forms.Select(attrs={'id': 'cidade'})
    )
    idAcao = forms.ModelChoiceField(queryset=AcaoExtensao.objects.all(), widget=forms.HiddenInput())
    endereco = EnderecoForm()
    class Meta:
        model = EdicaoAcao
        fields = [
            'idAcao',
            'numEdicao',
            'nomeEdicao',
            'dtModificacao',
            'dtInicio',
            'dtFim',
            'idEstado',
            'idCidade',
        ]
        widgets = {
           
            'dtModificacao': forms.DateInput(attrs={'type': 'date'}),
            'dtInicio': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'dtFim': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'idEstado': forms.Select(attrs={'class': 'form-control', 'id': 'estado'}),
            'idCidade': forms.Select(attrs={'class': 'form-control', 'id': 'cidade'})
        }

    def save(self, commit=True):
      
        EdicaoAcao = super().save(commit=False)
        
        endereco_form = self.cleaned_data.get('endereco')

        if 'idEstado' in self.data:
            try:
                estado_id = int(self.data.get('idEstado'))
                self.fields['idCidade'].queryset = Cidades.objects.filter(UF_id=estado_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['idCidade'].queryset = self.instance.UF.cidades_set.all()

        if endereco_form:
            endereco = Endereco.objects.create(**endereco_form)
            EdicaoAcao.idEndereco = endereco

        if commit:
            EdicaoAcao.save()

        return EdicaoAcao

    
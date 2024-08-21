from django import forms
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import AcaoExtensao,TipoAcao,SituacaoAcao, Estados, Cidades, EdicaoAcao
from datetime import datetime
from .forms import AcaoExtensaoForm, ContatoForm, EdicaoAcaoForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib import messages
def cidades_por_estado(request, idEstado):
    cidades = Cidades.objects.filter(UF=idEstado).values('idCidade', 'Cidade')
    return JsonResponse({'cidades': list(cidades)})

def criarAcao(request, pk=None):
    if pk:
        acao_extensao = get_object_or_404(AcaoExtensao, pk=pk)
    else:
        acao_extensao = None

    if request.method == 'POST':
        form = AcaoExtensaoForm(request.POST, request.FILES, instance=acao_extensao)
        if form.is_valid():
            try:
                acao_extensao = form.save()
                messages.success(request, 'Cadastro da Ação de Extensão concluído com sucesso!')
                return redirect('extensoes')  
            except forms.ValidationError as e:
                messages.error(request, f'Erro: {e}')
    else:
        form = AcaoExtensaoForm(instance=acao_extensao)

    return render(request, 'criarAcao.html', {'form': form})

def criarEdicao(request, pk=None):
    if pk:
        edicao_acao = get_object_or_404(EdicaoAcao, pk=pk)
    else:
        edicao_acao = EdicaoAcao()

    if request.method == 'POST':
        formEdicao = EdicaoAcaoForm(request.POST, instance=edicao_acao)
        if formEdicao.is_valid():
            formEdicao.save()
            messages.success(request, 'Edição de Ação concluída com sucesso!')
            return redirect('extensoes')  
    else:
        formEdicao = EdicaoAcaoForm(instance=edicao_acao)

    return render(request, 'criarEdicao.html', {'formEdicao': formEdicao})
def index(request):
    estados = Estados.objects.all()
    return render(request, 'index.html', {'estados': estados})

def menu(request):
    return render(request, 'menu.html')

def footer(request):
    return render(request, 'footer.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    if request.method == 'POST':
        contato_form = ContatoForm(request.POST, prefix='contato')
        if contato_form.is_valid():
            contato_form.save()
    else:
        contato_form = ContatoForm(prefix='contato')
        messages.success(request, 'Contato registrado, espere pelo contato de um de nossos administradores!')   
    return render(request, 'contato.html', {
        'contato_form': contato_form
    })

def projeto(request, idAcao):
    tipos = TipoAcao.objects.all()
    situacoes = SituacaoAcao.objects.all()
    acoes = AcaoExtensao.objects.all()
    edicao = EdicaoAcao.objects.filter(idAcao=idAcao)

    projeto = get_object_or_404(AcaoExtensao, idAcao=idAcao)
    return render(request, 'projeto.html',{
    'acoes': acoes,
    'tipos': tipos,
    'situacoes': situacoes,
    'projeto': projeto,
    'edicao':edicao
    })
def extensoes(request):
    search_term = request.GET.get('search', '')
    search_situacao = request.GET.get('situacao', '')
    search_estado = request.GET.get('Estados', '')
    search_tipo = request.GET.get('tipo', '')
    order_direction = request.GET.get('order_direction', 'asc') 
    data_inicio = request.GET.get('data_inicio', '')
    data_fim = request.GET.get('data_fim', '')
    tipos = TipoAcao.objects.all()
    situacoes = SituacaoAcao.objects.all()
    estados = Estados.objects.all()

    filtros = Q()
    
    if search_situacao:
        filtros &= Q(idSituacao__idSituacao=search_situacao)
    if search_estado:
        filtros &= Q(idEstado__idEstado=search_estado)
    if search_tipo:
        filtros &= Q(idTipo__idTipo=search_tipo)
    if data_inicio:
        try:
            data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
            filtros &= Q(dtInicio__gte=data_inicio)
        except ValueError:
            pass 
    if data_fim:
        try:
            data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
            filtros &= Q(dtFim__lte=data_fim)
        except ValueError:
            pass  

    acoes = AcaoExtensao.objects.filter(
        filtros &
        (Q(TituloAcao__icontains=search_term) |
         Q(coordenadorAcao__icontains=search_term) |
         Q(alunoAcao__icontains=search_term) |
         Q(idTipo__nomeTipo__icontains=search_term) |
         Q(idSituacao__nomeSituacao__icontains=search_term))
    )

    if order_direction == 'desc':
        acoes = acoes.order_by('-dtCriacao')
    else:
        acoes = acoes.order_by('dtCriacao')

    return render(request, 'extensoes.html', {
        'acoes': acoes,
        'search_term': search_term,
        'search_situacao': search_situacao,
        'search_localizacao': search_estado,
        'search_tipo': search_tipo,
        'order_direction': order_direction,
        'tipos': tipos,
        'situacoes': situacoes,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
        'estados':estados
    })


from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import AcaoExtensao,TipoAcao,SituacaoAcao, Estados, Cidades
from datetime import datetime
from .forms import AcaoExtensaoForm
from django.http import JsonResponse

def cidades_por_estado(request, idEstado):
    cidades = Cidades.objects.filter(UF=idEstado).values('idCidade', 'Cidade')
    return JsonResponse({'cidades': list(cidades)})

def criarAcao(request):
    
    if request.method == 'POST':
        form = AcaoExtensaoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AcaoExtensaoForm()
    return render(request, 'criarAcao.html', {'form': form})

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
    return render(request, 'contato.html')


def projeto(request, idAcao):
    tipos = TipoAcao.objects.all()
    situacoes = SituacaoAcao.objects.all()
    acoes = AcaoExtensao.objects.all()
    projeto = get_object_or_404(AcaoExtensao, idAcao=idAcao)
    return render(request, 'projeto.html',{
    'acoes': acoes,
    'tipos': tipos,
    'situacoes': situacoes,
    'projeto': projeto,
    })
 
def extensoes(request):
    search_term = request.GET.get('search', '')
    search_situacao = request.GET.get('situacao', '')
    search_localizacao = request.GET.get('localizacao', '')
    search_tipo = request.GET.get('tipo', '')
    order_direction = request.GET.get('order_direction', 'asc') 
    data_inicio = request.GET.get('data_inicio', '')
    data_fim = request.GET.get('data_fim', '')
    tipos = TipoAcao.objects.all()
    situacoes = SituacaoAcao.objects.all()

    filtros = Q()
    
    if search_situacao:
        filtros &= Q(idSituacao__idSituacao=search_situacao)
    if search_localizacao:
        filtros &= Q(localizacao__icontains=search_localizacao)
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
        'search_localizacao': search_localizacao,
        'search_tipo': search_tipo,
        'order_direction': order_direction,
        'tipos': tipos,
        'situacoes': situacoes,
        'data_inicio': data_inicio,
        'data_fim': data_fim
    })


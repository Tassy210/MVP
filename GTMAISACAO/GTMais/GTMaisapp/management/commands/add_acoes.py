from django.core.management.base import BaseCommand
from GTMaisapp.models import AcaoExtensao, TipoAcao, SituacaoAcao, EdicaoAcao
from django.utils import timezone
from datetime import datetime

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de exemplo'

    def handle(self, *args, **kwargs):
        # Adiciona TipoAcao
        tipo_acao1, created = TipoAcao.objects.get_or_create(
            idTipo=1,
            defaults={'nomeTipo': 'Tipo de Exemplo 1'}
        )
        tipo_acao2, created = TipoAcao.objects.get_or_create(
            idTipo=2,
            defaults={'nomeTipo': 'Tipo de Exemplo 2'}
        )

        # Adiciona SituacaoAcao
        situacao_acao1, created = SituacaoAcao.objects.get_or_create(
            idSituacao=1,
            defaults={'nomeSituacao': 'Situação de Exemplo 1'}
        )
        situacao_acao2, created = SituacaoAcao.objects.get_or_create(
            idSituacao=2,
            defaults={'nomeSituacao': 'Situação de Exemplo 2'}
        )

        # Adiciona AcaoExtensao
        acao = AcaoExtensao.objects.create(
            TituloAcao='Ação de Exemplo',
            coordenadorAcao='Carlos Souza',
            alunoAcao='Ana Pereira',
            idTipo=tipo_acao1,
            idSituacao=situacao_acao1,
            dtCriacao=datetime.strptime('2024-02-01', '%Y-%m-%d').date(),
            dtModificacao=datetime.strptime('2024-02-02', '%Y-%m-%d').date(),
            dtInicio=datetime.strptime('2024-02-15 09:00:00', '%Y-%m-%d %H:%M:%S'),
            dtFim=datetime.strptime('2024-02-20 18:00:00', '%Y-%m-%d %H:%M:%S'),
            localizacao='Sala de Reuniões'
        )

        # Adiciona EdicaoAcao
        EdicaoAcao.objects.create(
            idAcao=acao,
            numEdicao=1,
            nomeEdicao='Edição de Exemplo 1'
        )

        self.stdout.write(self.style.SUCCESS('Dados adicionados com sucesso!'))

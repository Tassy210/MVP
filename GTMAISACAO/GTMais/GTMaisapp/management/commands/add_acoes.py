from django.core.management.base import BaseCommand
from GTMaisapp.models import AcaoExtensao, TipoAcao, SituacaoAcao, EdicaoAcao, Cidades, Estados
from django.utils import timezone
from datetime import datetime

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados de exemplo'

    def handle(self, *args, **kwargs):
    
        tipo_acao1, created = TipoAcao.objects.get_or_create(
            idTipo=1,
            defaults={'nomeTipo': 'Evento'}
        )
        tipo_acao2, created = TipoAcao.objects.get_or_create(
            idTipo=2,
            defaults={'nomeTipo': 'Curso'}
        )

        situacao_acao1, created = SituacaoAcao.objects.get_or_create(
            idSituacao=1,
            defaults={'nomeSituacao': 'Completo'}
        )
        situacao_acao2, created = SituacaoAcao.objects.get_or_create(
            idSituacao=2,
            defaults={'nomeSituacao': 'Incompleto'}
        )
        tipo_acao_instance = TipoAcao.objects.get(pk=2)
        estado_acao_instance = Estados.objects.get(pk=5)
        Cidades_acao_instance = Cidades.objects.get(pk=28)
        situacao_acao_instance = SituacaoAcao.objects.get(pk=1)

        AcaoExtensao1, created = AcaoExtensao.objects.get_or_create(
            idAcao=1,
            defaults={
                'TituloAcao': 'Educação e Sustentabilidade: Construindo um Futuro Verde',
                'coordenadorAcao': 'Completo',
                'alunoAcao': 'Cleiton Rodrigues',
                'descricao': 'Valdisnei W. e Juliano Julião',
                'idTipo': tipo_acao_instance,
                'dtCriacao': datetime(2024, 8, 13),
              
              
            }
)

        self.stdout.write(self.style.SUCCESS('Dados adicionados com sucesso!'))

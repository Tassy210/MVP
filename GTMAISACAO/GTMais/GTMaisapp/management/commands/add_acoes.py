from django.core.management.base import BaseCommand
from GTMaisapp.models import AcaoExtensao, TipoAcao, SituacaoAcao, EdicaoAcao, Cidades
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


        self.stdout.write(self.style.SUCCESS('Dados adicionados com sucesso!'))

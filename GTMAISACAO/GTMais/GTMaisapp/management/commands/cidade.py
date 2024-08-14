
import requests
from django.core.management.base import BaseCommand
from GTMaisapp.models import Estados, Cidades

class Command(BaseCommand):
    help = 'Obtém e insere cidades e estados na base de dados'

    def handle(self, *args, **kwargs):
        url = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            
            for municipio in data:  
         
                estado_data = municipio.get('municipio', {}).get('microrregiao', {}).get('mesorregiao', {}).get('UF', {})
                estado_sigla = estado_data.get('sigla', 'Sigla não disponível')
                estado_nome = estado_data.get('nome', 'Nome não disponível')
                
                estado, created = Estados.objects.get_or_create(UF=estado_sigla, defaults={'Estado': estado_nome})
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Estado criado: {estado.Estado} ({estado.UF})'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Estado existente: {estado.Estado} ({estado.UF})'))
                
                cidade_nome = municipio.get('nome', 'Nome não disponível')
                
                cidade, created = Cidades.objects.get_or_create(Cidade=cidade_nome, UF=estado)
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Cidade criada: {cidade.Cidade} - {cidade.UF.UF}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Cidade existente: {cidade.Cidade} - {cidade.UF.UF}'))
        else:
            self.stdout.write(self.style.ERROR(f'Erro na requisição: {response.status_code}'))

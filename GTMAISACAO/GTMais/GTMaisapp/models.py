from django.db import models
from django.utils import timezone
import datetime

class SituacaoAcao(models.Model):
    idSituacao = models.AutoField(primary_key=True)
    nomeSituacao = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nomeSituacao} ({self.idSituacao})'


class TipoAcao(models.Model):
    idTipo = models.AutoField(primary_key=True)
    nomeTipo = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nomeTipo} ({self.idTipo})'

class Estados(models.Model):
    idEstado = models.AutoField(primary_key=True)
    UF = models.CharField(max_length=255)
    Estado = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.UF} ({self.Estado})'

class Cidades(models.Model):
    idCidade = models.AutoField(primary_key=True)
    Cidade = models.CharField(max_length=255)
    UF = models.ForeignKey(Estados, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.idCidade} ({self.Cidade})'

class AcaoExtensao(models.Model):
    idAcao = models.AutoField(primary_key=True)
    TituloAcao = models.CharField(max_length=255)
    descricao = models.CharField(max_length=500)
    coordenadorAcao = models.CharField(max_length=255)
    alunoAcao = models.CharField(max_length=255)
    idTipo = models.ForeignKey(TipoAcao, on_delete=models.CASCADE)
    idSituacao = models.ForeignKey(SituacaoAcao, on_delete=models.CASCADE)
    dtCriacao = models.DateField(null=True, blank=True)
    dtModificacao = models.DateField(null=True, blank=True)
    dtInicio = models.DateTimeField(default=datetime.datetime.now)
    dtFim = models.DateTimeField(null=True, blank=True)
    CEP = models.CharField(max_length=255)
    idEstado= models.ForeignKey(Estados, on_delete=models.CASCADE)
    idCidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    Numero= models.SmallIntegerField()
    Complemento= models.CharField(max_length=255)
    Rua= models.CharField(max_length=255)
    Bairro= models.CharField(max_length=255)
 

    def __str__(self):
        return self.TituloAcao


class EdicaoAcao(models.Model):
    idEdicao = models.AutoField(primary_key=True)
    idAcao = models.ForeignKey(AcaoExtensao, on_delete=models.CASCADE)
    numEdicao = models.SmallIntegerField()
    nomeEdicao = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nomeEdicao} ({self.numEdicao})'


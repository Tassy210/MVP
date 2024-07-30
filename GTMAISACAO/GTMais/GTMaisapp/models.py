from django.db import models
from django.utils import timezone

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


class AcaoExtensao(models.Model):
    idAcao = models.AutoField(primary_key=True)
    TituloAcao = models.CharField(max_length=255)
    coordenadorAcao = models.CharField(max_length=255)
    alunoAcao = models.CharField(max_length=255)
    idTipo = models.ForeignKey(TipoAcao, on_delete=models.CASCADE)
    idSituacao = models.ForeignKey(SituacaoAcao, on_delete=models.CASCADE)
    dtCriacao = models.DateField(null=True, blank=True)
    dtModificacao = models.DateField(null=True, blank=True)
    dtInicio = models.DateTimeField()
    dtFim = models.DateTimeField(null=True, blank=True)
    localizacao = models.CharField(max_length=255)

    def __str__(self):
        return self.TituloAcao


class EdicaoAcao(models.Model):
    idEdicao = models.AutoField(primary_key=True)
    idAcao = models.ForeignKey(AcaoExtensao, on_delete=models.CASCADE)
    numEdicao = models.SmallIntegerField()
    nomeEdicao = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nomeEdicao} ({self.numEdicao})'

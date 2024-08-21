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

class Pessoa(models.Model):
    idPessoa= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20) 
    dataNascimento = models.DateField(null=True, blank=True)
 
    def __str__(self):
        return f'{self.idPessoa} ({self.nome})'

class Usuario(models.Model):
    idUsuario= models.AutoField(primary_key=True)
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    permissao = models.CharField(max_length=255)
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.idUsuario} ({self.email})'
    

class AreaConhecimento(models.Model):
    codAreaConhecimento= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.codAreaConhecimento} ({self.nome})'
    
class Curso(models.Model):
    codCurso= models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.codCurso} ({self.nome})'

class Endereco(models.Model):
    idEndereco = models.AutoField(primary_key=True)
    CEP = models.CharField(max_length=255)
    numero= models.SmallIntegerField()
    complemento= models.CharField(max_length=255)
    rua= models.CharField(max_length=255)
    bairro= models.CharField(max_length=255)

    def __str__(self):
        return self.rua

class AcaoExtensao(models.Model):
    idAcao = models.AutoField(primary_key=True)
    TituloAcao = models.CharField(max_length=255)
    descricao = models.CharField(max_length=500)
    coordenadorAcao = models.CharField(max_length=255)
    alunoAcao = models.CharField(max_length=255)
    dtCriacao = models.DateField(null=True, blank=True)
    imagem = models.ImageField(upload_to='projectsimages/')
    idTipo = models.ForeignKey(TipoAcao, on_delete=models.CASCADE)
    idSituacao = models.ForeignKey(SituacaoAcao, on_delete=models.CASCADE)
    idEndereco= models.ForeignKey(Endereco, on_delete=models.CASCADE)
    contato= models.CharField(max_length=255)
    aceitaContribuicoes = models.BooleanField(default=True) 
    artigo= models.CharField(max_length=255)
    idEstado= models.ForeignKey(Estados, on_delete=models.CASCADE)
    idCidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    def __str__(self):
        return self.TituloAcao


class ImagemAcao(models.Model):
    acao_extensao = models.ForeignKey(AcaoExtensao, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='projectsimages/')
    
    def __str__(self):
        return f'Imagem {self.id} para {self.acao_extensao.TituloAcao}'



class EdicaoAcao(models.Model):
    idEdicao = models.AutoField(primary_key=True)
    idAcao = models.ForeignKey(AcaoExtensao, on_delete=models.CASCADE)
    numEdicao = models.SmallIntegerField()
    nomeEdicao = models.CharField(max_length=255)
    idEstado= models.ForeignKey(Estados, on_delete=models.CASCADE)
    idCidade = models.ForeignKey(Cidades, on_delete=models.CASCADE)
    dtModificacao = models.DateField(null=True, blank=True)
    dtInicio = models.DateTimeField(default=datetime.datetime.now)
    dtFim = models.DateTimeField(null=True, blank=True)
    idEndereco= models.ForeignKey(Endereco, on_delete=models.CASCADE)
    coordenadorEdicao = models.CharField(max_length=255)
    contato= models.CharField(max_length=255)
    alunoEdicao = models.CharField(max_length=255)
    def __str__(self):
        return f'{self.nomeEdicao} ({self.numEdicao})'

class ContatoAcao(models.Model):
    idContato = models.AutoField(primary_key=True)
    nome=models.CharField(max_length=255)
    telefone=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    titulo=models.CharField(max_length=255)
    descricao=models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.idContato} ({self.nome})'

class ImagemContato(models.Model):
    Contato_Acao = models.ForeignKey(ContatoAcao, related_name='imagens', on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='contactsimages/')
    

    def __str__(self):
        return f'Imagem {self.id} para {self.contato_acao.nome}'   
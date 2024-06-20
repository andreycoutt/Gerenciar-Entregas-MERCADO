from re import VERBOSE
from django.db import models

# Create your models here.

class CadastrarCliente(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    cpf = models.IntegerField(primary_key=True, verbose_name="CPF", unique=True)
    telefone = models.IntegerField(verbose_name="Telefone")
    endereco = models.CharField(max_length=150, verbose_name="Endereço")
    
  
    def __str__(self):
      return "{} {} {} {}".format(self.nome, self.cpf, self.telefone, self.endereco)

class CadastrarEntrega(models.Model):
  nome = models.CharField(max_length=100, verbose_name="Nome")
  endereco = models.CharField(max_length=150, verbose_name="Endereço")
  caixas = models.IntegerField(verbose_name="Caixas")
  volumeextra = models.CharField(max_length=150, verbose_name="Volume Extra", blank=True, null=True, default="")
  nomeembalador = models.CharField(max_length=100, verbose_name="Nome do Embalador")
  datacompra = models.DateField(verbose_name="Data da Compra")
  dataentrega = models.DateField(verbose_name="Data da Entrega")


  def __str__(self):
    return "{} {} {} {} {} {} {}".format(self.nome, self.endereco, self.caixas, self.volumeextra, self.nomeembalador, self.datacompra, self.dataentrega)
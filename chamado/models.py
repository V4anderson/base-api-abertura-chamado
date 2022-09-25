from django.db import models

class Chamado(models.Model):
    num_os = models.CharField("Número da O.S",max_length=6)
    nome_completo = models.CharField("Nome Completo",max_length=50)
    cpf_cnpj = models.CharField("CPF/CNPJ",max_length=18)
    endereco = models.CharField("Endereço",max_length=250)
    bairro = models.CharField("Bairro",max_length=120)
    cidade = models.CharField("Cidade",max_length=120)
    telefone = models.CharField("Telefone",max_length=14)
    tipo_de_servico = models.CharField("Tipo de Serviço",max_length=250)


    def __str__(self):
     return self.num_os   
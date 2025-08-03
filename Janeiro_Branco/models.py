from django.db import models
from django.contrib.auth.models import User

class Mensagem(models.Model):
    conteudo = models.TextField()

    data_criacao = models.DateTimeField(auto_now_add=True)

    #chave estrangeira que liga esta mensagem a um usuário
    #se o usuário for deletado, todas as suas mensagens também serão (on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    #um campo booleano (Verdadeiro/Falso) para a opção de postar anonimamente
    exibir_anonimo = models.BooleanField(default=False)

    #o campo para o "Soft Delete". Por padrão, é verdadeiro, ou seja, a mensagem está visível
    esta_visivel = models.BooleanField(default=True)

    def __str__(self):
        #define como o objeto será exibido no painel de administração do Django
        return f'Mensagem de {self.autor.username} em {self.data_criacao.strftime("%d/%m/%Y")}'
    
class Recomendacao(models.Model):
    nome_site_app = models.CharField(max_length=200)
    url = models.URLField()
    descricao = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creditar_autor = models.BooleanField(default=True)

class RegiaoAdministrativa(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class LocalAtendimento(models.Model):
    #filtros
    class TipoAtendimento(models.TextChoices):
        PRESENCIAL = 'PRESENCIAL', 'Presencial'
        ONLINE = 'ONLINE', 'Online'
        AMBOS = 'AMBOS', 'Ambos'

    class FormaPagamento(models.TextChoices):
        GRATUITO = 'GRATUITO', 'Gratuito'
        SOCIAL = 'SOCIAL', 'Preço Social'
        INTEIRO = 'INTEIRO', 'Preço Inteiro'

    #campos de informações para o modelo
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=255)
    contato = models.CharField(max_length=50, blank=True)
    site = models.URLField(max_length=200, blank=True)
    
    #relacionamento com a região administrativa
    regiao_administrativa = models.ForeignKey(RegiaoAdministrativa, on_delete=models.CASCADE, related_name='locais')
    
    #campos para os filtros
    tipo_atendimento = models.CharField(
        max_length=10,
        choices=TipoAtendimento.choices,
        default=TipoAtendimento.PRESENCIAL
    )
    forma_pagamento = models.CharField(
        max_length=10,
        choices=FormaPagamento.choices,
        default=FormaPagamento.INTEIRO
    )

    #campos para o mapa
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.nome


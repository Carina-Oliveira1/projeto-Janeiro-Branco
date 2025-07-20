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


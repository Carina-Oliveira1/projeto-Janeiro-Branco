from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Mensagem, Recomendacao

#essa é uma classe de formulário que herda
#no UserCreationForm padrão do Django. Fazemos isso para poder customizá-lo
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #especificamos que este formulário está relacionado ao modelo de usuário padrão do Django
        model = User
        
        #definimos quais campos do modelo User queremos exibir no formulário
        #o Django cuidará automaticamente dos campos de senha e confirmação de senha
        fields = ('username', 'email')

class MensagemForm(forms.ModelForm):
    class Meta:
        model = Mensagem
        #estes são os campos do modelo que aparecerão no formulário
        fields = ['conteudo', 'exibir_anonimo']
        labels = {
            'conteudo': 'Sua mensagem de apoio',
            'exibir_anonimo': 'Desejo que minha mensagem seja exibida como "Anônimo"'
        }
        widgets = {
            'conteudo': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Escreva algo positivo...'}),
        }

class RecomendacaoForm(forms.ModelForm):
    class Meta:
        model = Recomendacao
        fields = ['nome_site_app', 'url', 'descricao', 'creditar_autor']
        labels = {
            'nome_site_app': 'Nome do Site ou App',
            'url': 'Link (URL)',
            'descricao': 'Por que você recomenda?',
            'creditar_autor': 'Quero que meu nome de usuário apareça como crédito'
        }
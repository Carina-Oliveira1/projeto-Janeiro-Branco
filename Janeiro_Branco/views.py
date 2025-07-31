from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, RecomendacaoForm, MensagemForm
from .models import Recomendacao, Mensagem
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'Janeiro_Branco/index.html')

def forum(request):
    return render(request, 'Janeiro_Branco/forum.html')

def login(request):
    return render(request, 'Janeiro_Branco/login.html')

def onde_encontrar_ajuda(request):
    return render(request, 'Janeiro_Branco/onde_encontrar_ajuda.html')

def somos(request):
    return render(request, 'Janeiro_Branco/somos.html')

def cadastro(request):
    return render(request, 'Janeiro_Branco/cadastro.html')

def cadastro(request):
    #essa linha verifica se o usuário está *enviando* o formulário (método POST)
    if request.method == 'POST':
        #se sim, cria uma instância do formulário com os dados que o usuário enviou (request.POST)
        form = CustomUserCreationForm(request.POST)
        
        #o django verifica se os dados são válidos (ex: o nome de usuário já não existe?)
        if form.is_valid():
            #se tudo estiver correto, salva o novo usuário no banco de dados
            form.save()
            #e redireciona o usuário para a página de login
            return redirect('login')
    #se o usuário está apenas *visitando* a página (método GET), não enviando dados
    else:
        #cria uma instância de um formulário vazio para ser exibido
        form = CustomUserCreationForm()
        
    #renderiza o arquivo html e envia o formulário (vazio ou com erros) para o template
    #o django vai procurar por 'Janeiro_Branco/cadastro.html' dentro da sua pasta 'templates'
    return render(request, 'Janeiro_Branco/cadastro.html', {'form': form})

def listar_recomendacoes(request):

    #busca os dados: acessa o modelo 'Recomendacao', pega todos os objetos (.all())
    #e os ordena pela data de envio, do mais novo para o mais antigo ('-data_envio')
    recomendacoes = Recomendacao.objects.all().order_by('-data_envio')

    #prepara o formulário: cria uma instância vazia do nosso RecomendacaoForm
    form = RecomendacaoForm()

    #prepara o "pacote de dados" (contexto) para enviar ao template
    #este dicionário terá duas chaves que poderão ser usadas no html
    contexto = {
            'lista_de_recomendacoes': recomendacoes,
            'form': form,
        }
    return render(request, 'Janeiro_Branco/recomendacoes.html', contexto)

@login_required #este "decorator" protege a view. Se o usuário não estiver logado, ele é automaticamente redirecionado para a página de login
def criar_recomendacao(request):

    #garante que a função só execute se o formulário for enviado
    if request.method == 'POST':
        #cria uma instância do formulário preenchida com os dados enviados pelo usuário
        form = RecomendacaoForm(request.POST)
        #roda todas as validações do Django (ex: a URL é válida? Os campos obrigatórios foram preenchidos?)
        if form.is_valid():
            #a linha abaixo cria o objeto Python, mas não o salva no banco ainda (commit=False).
            #isso é crucial porque precisamos adicionar o autor antes de salvar
            recomendacao = form.save(commit=False)
            
            # aribuímos o usuário que está logado na sessão (request.user) ao campo 'autor' do objeto
            recomendacao.autor = request.user
            
            # aora, com o autor definido, salvamos o objeto completo no banco de dados
            recomendacao.save()
            
            # aós salvar com sucesso, redireciona o usuário de volta para a lista de recomendações
            return redirect('listar_recomendacoes')

    #se a requisição não for *post*, apenas redireciona de volta para a lista.
    return redirect('listar_recomendacoes')

def forum(request):
    mensagens_visiveis = Mensagem.objects.filter(esta_visivel=True).order_by('-data_criacao')
    #cria uma instância de um formulário vazio para ser passada ao template
    form_mensagem = MensagemForm() 
    contexto = {
        'lista_de_mensagens': mensagens_visiveis,
        'form': form_mensagem, #passa o formulário para o template
    }
    return render(request, 'Janeiro_Branco/forum.html', contexto)

@login_required
def criar_mensagem(request):
    if request.method == 'POST':
        form = MensagemForm(request.POST)
        if form.is_valid():
            mensagem = form.save(commit=False)
            mensagem.autor = request.user
            mensagem.save()
            return redirect('forum')
    return redirect('forum')

@login_required
#soft delete
def deletar_mensagem(request, mensagem_id):
    mensagem = get_object_or_404(Mensagem, pk=mensagem_id)
    if request.user == mensagem.autor:
        mensagem.esta_visivel = False
        mensagem.save()
    return redirect('forum')
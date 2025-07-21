from django.urls import path
from Janeiro_Branco.views import index, explore, forum, login, onde_encontrar_ajuda, somos, entenda_mais, cadastro
from . import views

urlpatterns = [
    path("", index, name="index"),
    path("explore/", explore, name="explore"),
    path("forum/", views.forum, name="forum"),
    path("login/", login, name="login"),
    path("onde_encontrar_ajuda/", onde_encontrar_ajuda, name="onde_encontrar_ajuda"),
    path("somos/", somos, name="somos"),
    path("entenda_mais/", entenda_mais, name="entenda_mais"),
    path("cadastro/", cadastro, name="cadastro"),
    path('recomendacoes/', views.listar_recomendacoes, name='listar_recomendacoes'),
    path('recomendacoes/criar/', views.criar_recomendacao, name='criar_recomendacao'),
    path('forum/mensagem/<int:mensagem_id>/excluir/', views.deletar_mensagem, name='deletar_mensagem'),
     path('forum/mensagem/criar/', views.criar_mensagem, name='criar_mensagem'),
]

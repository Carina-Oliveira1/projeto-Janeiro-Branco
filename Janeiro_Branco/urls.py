from django.urls import path
from Janeiro_Branco.views import index, onde_encontrar_ajuda, somos, cadastro
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index, name="index"),
    path("forum/", views.forum, name="forum"),
    path('login/', auth_views.LoginView.as_view(template_name='Janeiro_Branco/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path("onde_encontrar_ajuda/", onde_encontrar_ajuda, name="onde_encontrar_ajuda"),
    path("somos/", somos, name="somos"),
    path("cadastro/", cadastro, name="cadastro"),
    path('recomendacoes/', views.listar_recomendacoes, name='listar_recomendacoes'),
    path('recomendacoes/criar/', views.criar_recomendacao, name='criar_recomendacao'),
    path('forum/mensagem/<int:mensagem_id>/excluir/', views.deletar_mensagem, name='deletar_mensagem'),
    path('forum/mensagem/criar/', views.criar_mensagem, name='criar_mensagem'),
    path('mapa/', views.mapa_view, name='mapa'),
    path('api/locais/', views.locais_api, name='locais_api'),
]

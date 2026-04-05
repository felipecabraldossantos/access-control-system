from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('cadastro_produto/', views.cadastro_produto, name='cadastro_produto'),
    path('produto/', views.produto, name='produto'),
    path('logout/', views.logout_view, name='logout'),
]
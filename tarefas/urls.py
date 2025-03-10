from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("atualizar/<str:primaryKey>/", views.atualizarTarefa, name='atualizar'),
    path("apagar/<str:primaryKey>/", views.deletarTarefa, name='deletar')
]
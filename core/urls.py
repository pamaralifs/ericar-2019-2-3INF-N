from django.urls import path
from .views import Index, InscricaoAluno, SucessoInscricaoAluno


app_name = 'core'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('inscricao/', InscricaoAluno.as_view(), name='inscricao_aluno'),
    path('sucesso/', SucessoInscricaoAluno.as_view(),
         name='sucesso_inscricao_aluno'),
]

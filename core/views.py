from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.views.generic.edit import FormView
from .models import Aluno
from .forms import AlunoFormInscricao
# Para salvar arquivo e para a view de download
from django.http import HttpResponse, Http404
from django.conf import settings
from os import path
import mimetypes

# Create your views here.


class Index(FormView):
    form_class = AlunoFormInscricao
    success_url = reverse_lazy('core:index')  # temporario pra ela mesmo
    template_name = 'core/index.html'
    model = Aluno

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        filtro1 = self.request.POST.get('email')
        #print('FILTRO1 ',filtro1)
        # print('passei')
        if Aluno.objects.filter(email=self.request.POST.get('email')):
            self.mensagem = 'Infelizmente não foi possível lhe inscrever!\\nJá existe um usuário inscrito com este e-mail.'
            return super().form_invalid(form)
        else:
            aluno_nome = self.request.POST.get('nome')
            aluno_email = self.request.POST.get('email')
            aluno_instrumento = self.request.POST.get('instrumento')
            aluno_msg = self.request.POST.get('mensagem')
            novo_aluno = Aluno(nome=aluno_nome, email=aluno_email,
                               instrumento=aluno_instrumento, mensagem=aluno_msg)
            novo_aluno.save()
            # salvar em arquivo texto

            nome_arquivo = "%s/%s" % (settings.BASE_DIR,
                                      'core/static/inscritos.txt')
            #print('NOME ARQUIVO: ',nome_arquivo)

            if not (path.exists(nome_arquivo)):
                arquivo = open(nome_arquivo, 'a', encoding='utf-8')
                arquivo.write('-----------------------------------\n')
                arquivo.write('GRANDES TALENTOS - ALUNOS INSCRITOS\n')
                arquivo.write('-----------------------------------\n')
            else:
                arquivo = open(nome_arquivo, 'a', encoding='utf-8')

            arquivo.write('Nome: ' + aluno_nome + '\n')
            arquivo.write('E-mail: ' + aluno_email + '\n')
            arquivo.write('Instrumento: ' + aluno_instrumento + '\n')
            arquivo.write('\n')
            arquivo.close()

            return super().form_valid(form)
        # return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        # Insere o form no contexto do template
        context['form'] = AlunoFormInscricao
        # print('TESTE',self.request.POST.get('email'))
        if not self.request.POST.get('email'):
            self.mensagem = ''
        context['mensagem'] = self.mensagem
        return context


class InscricaoAluno(CreateView):
    template_name = 'core/inscricao_aluno.html'


class SucessoInscricaoAluno(TemplateView):
    template_name = 'core/sucesso_inscricao_aluno.html'

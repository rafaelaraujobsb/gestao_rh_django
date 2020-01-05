from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from .models import Funcionario


# @login_required
# def home(request):
#     return HttpResponse('Olá')


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False) # Não enviar o objeto para o BD
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username="".join(funcionario.nome.split(" ")[:2]))
        funcionario.save()

        return super().form_valid(form)

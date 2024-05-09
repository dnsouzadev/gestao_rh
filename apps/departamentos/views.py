from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView

from apps.departamentos.models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    # def get_queryset(self):
    #     empresa_logada = self.request.user.funcionario.empresa
    #     return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']
    success_url = '/departamentos/list'

    # def get_queryset(self):
    #     empresa_logada = self.request.user.funcionario.empresa
    #     return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = '/departamentos/list'

    # def get_queryset(self):
    #     empresa_logada = self.request.user.funcionario.empresa
    #     return Departamento.objects.filter(empresa=empresa_logada)
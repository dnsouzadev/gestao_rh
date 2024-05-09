from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import Departamento


class DepartamentosList(ListView):
    model = Departamento

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome']
    success_url = '/departamentos/list'

    def form_valid(self, form):
        departamento = form.save(commit=False)
        empresa_logada = self.request.user.funcionario.empresa
        departamento.empresa = empresa_logada
        departamento.save()
        return super(DepartamentoCreate, self).form_valid(form)


class DepartamentoUpdate(UpdateView):
    model = Departamento
    fields = ['nome']
    success_url = '/departamentos/list'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)


class DepartamentoDelete(DeleteView):
    model = Departamento
    success_url = '/departamentos/list'

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Departamento.objects.filter(empresa=empresa_logada)

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView

from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']

    def form_valid(self, form):
        hora_extra = form.save(commit=False)
        hora_extra.registrado_por = self.request.user
        hora_extra.save()
        return super(HoraExtraCreate, self).form_valid(form)


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra

    def get_success_url(self):
        return reverse_lazy('list_hora_extra')
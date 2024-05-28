from io import BytesIO

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from reportlab.pdfgen import canvas

from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = reverse_lazy('list_funcionarios')

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']
    success_url = reverse_lazy('list_funcionarios')

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(
            username=funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1])
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


def test_view(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'

    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(150, 810, 'Relatório de Funcionários')

    funcionarios = Funcionario.objects.all()

    str = 'Nome: %s | Hora Extra: %s'

    y = 750
    for funcionario in funcionarios:
        print(funcionario.nome, funcionario.total_horas_extra)
        p.drawString(10, y, str % (funcionario.nome, funcionario.total_horas_extra))
        y -= 50

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response

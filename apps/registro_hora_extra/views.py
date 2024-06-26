import csv
import json

import xlwt
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from .forms import RegistroHoraExtraForm
from apps.registro_hora_extra.models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra

    def get_success_url(self):
        return reverse_lazy('list_hora_extra')


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm

    # success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):
        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        if not registro_hora_extra.utilizada:
            registro_hora_extra.utilizada = True
        else:
            registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        # Recalcular total_horas_extra do empregado
        empregado = self.request.user.funcionario

        response = json.dumps({
            'mensagem': 'Requisição POST',
            'pk': kwargs['pk'],
            'utilizada': registro_hora_extra.utilizada,
            'horas': float(empregado.total_horas_extra),
            'funcionario': empregado.nome
        })
        return HttpResponse(response, content_type='application/json')


class ExportarParaCSV(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="relatorio.csv"'

        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        header = ['Id', 'Funcionário', 'Motivo', 'Horas Restantes', 'Horas Totais']
        writer = csv.writer(response)
        writer.writerow(header)

        for registro in registros:
            writer.writerow([registro.id, registro.funcionario, registro.motivo, registro.horas,
                             registro.funcionario.total_horas_extra])
        return response


class ExportExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Banco de Horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Id', 'Funcionário', 'Motivo', 'Horas Restantes', 'Horas Totais']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.funcionario.nome, font_style)
            ws.write(row_num, 2, registro.motivo, font_style)
            ws.write(row_num, 3, registro.horas, font_style)
            ws.write(row_num, 4, registro.funcionario.total_horas_extra, font_style)
            row_num += 1

        wb.save(response)
        return response

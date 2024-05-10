from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from apps.documentos.models import Documento
from apps.funcionarios.models import Funcionario


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    # template_name = 'documentos/documento_form.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.pertence_id = self.kwargs['funcionario_id']
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    # def form_valid(self, form):
    #     funcionario = Funcionario.objects.get(id=1)
    #     form.instance.pertence = funcionario
    #     return super(DocumentoCreate, self).form_valid(form)

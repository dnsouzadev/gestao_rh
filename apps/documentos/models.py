from django.db import models
from django.urls import reverse_lazy

from apps.funcionarios.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField(max_length=100)
    pertence = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    arquivo = models.FileField(upload_to='documentos')

    def get_absolute_url(self):
        return reverse_lazy('edit_funcionarios', kwargs={'pk': self.pertence.id})

    def __str__(self):
        return self.descricao

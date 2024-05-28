from django.urls import path, include
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioCreate, pdf_view, Pdf

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionarios'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionarios'),
    path('criar', FuncionarioCreate.as_view(), name='create_funcionarios'),
    path('relatorios_funcionarios/', pdf_view, name='relatorio_funcionarios'),
    path('relatorios_funcionarios_html/', Pdf.as_view(), name='relatorio_funcionarios_html'),
]

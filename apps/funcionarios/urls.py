from django.urls import path, include
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioCreate, test_view

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionarios'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionarios'),
    path('criar', FuncionarioCreate.as_view(), name='create_funcionarios'),
    path('pdf-view/', test_view, name='pdf_funcionarios'),
]

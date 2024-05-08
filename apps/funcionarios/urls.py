from django.urls import path, include
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionarios'),
    path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionarios'),
]

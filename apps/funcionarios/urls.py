from django.urls import path, include
from .views import FuncionariosList, FuncionarioEdit

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('editar/<int:pk>', FuncionarioEdit.as_view(), name='edit_funcionarios'),
]

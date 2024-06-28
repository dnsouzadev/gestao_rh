from django.urls import path, include
from .views import DocumentoCreate, DocumentoUpdate, DocumentoDelete

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoCreate.as_view(), name='create_documento'),
    path('editar/<int:pk>', DocumentoUpdate.as_view(), name='update_documento'),
    path('deletar/<int:pk>', DocumentoDelete.as_view(), name='delete_documento'),
]

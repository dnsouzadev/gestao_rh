from django.urls import path, include
from .views import DepartamentosList

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('create/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),
    path('update/<int:pk>/', DepartamentoEdit.as_view(), name='update_departamento'),

]

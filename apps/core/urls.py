from django.urls import path, include
from .views import home, UserViewSet, GroupViewSet, celery
from rest_framework import routers
from apps.funcionarios.api.views import FuncionarioViewSet
from apps.registro_hora_extra.api.views import BancoHorasViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'banco-horas', BancoHorasViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api-auth/', include(router.urls)),
    path('celery/', celery, name='celery'),
]

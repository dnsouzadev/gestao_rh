from django.urls import path, include
from .views import home, UserViewSet, GroupViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('api-auth/', include(router.urls)),
]

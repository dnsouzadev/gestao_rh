from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .serializers import GroupSerializer, UserSerializer
from .tasks import send_relatorio


@login_required
def home(request):
    data = {'usuario': request.user}
    return render(request, 'core/index.html', data)


def register(request):
    form = UserCreationForm()
    data = {'form': form}
    return render(request, 'registration/register.html', data)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


def celery(request):
    send_relatorio.delay()
    return HttpResponse('Relatório sendo gerado em background')

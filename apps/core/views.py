from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.funcionarios.models import Funcionario


@login_required
def home(request):
    data = {'usuario': request.user}
    return render(request, 'core/index.html', data)

def register(request):
    form = UserCreationForm()
    data = {'form': form}
    return render(request, 'registration/register.html', data)
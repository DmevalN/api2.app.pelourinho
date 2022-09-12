from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    bem_vimdo = 'seja bem vindo'
    
    return render(request, 'administrador/index.html', {'bem_vimdo': bem_vimdo})

@permission_classes([IsAuthenticated])
def cadastrar(request):
    return render(request, 'administrador/cadastrar.html')
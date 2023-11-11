from django.http import HttpResponse
from django.shortcuts import render #permet de chercher un template et faire le rendu

# Create your views here.


def index (request):
    return render(request, 'main/index.html')


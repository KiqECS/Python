from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("Olá, esse é o meu primeiro projeto em Django")
from django.shortcuts import render
from django.http import HttpResponse
from algorithm_app import MainProgram

# Create your views here.
def success(request):
    MainProgram.mainProgram()
    return HttpResponse('This is algorithm app')
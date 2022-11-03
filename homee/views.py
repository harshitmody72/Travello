from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home1(request):
    return HttpResponse('Hello Worl')


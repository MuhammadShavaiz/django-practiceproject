from django.shortcuts import render
from django.http import HttpResponse

def home2(request):
    return HttpResponse('this is the home page for blog')
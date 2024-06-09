from django.shortcuts import render
from django.http import HttpResponse
def say_hello(request):
    return HttpResponse('Hello, this is the first page')
def about(request):
    return HttpResponse("This is About page")
def youtube(request):
    return HttpResponse('''<h1>shavaiz</h1><a href = "https://www.youtube.com">visit youtube!</a>''')

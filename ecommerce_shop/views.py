from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, "about.html")
def contact(request):
    return HttpResponse("this is contact")
def tracker(request):
    return HttpResponse("this is tracker")
def checkout(request):
    return HttpResponse("this is checkout")
def productView(request):
    return HttpResponse("this is productView")
def search(request):
    return HttpResponse("this is search")

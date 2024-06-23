from math import ceil
from django.shortcuts import render
from django.http import HttpResponse
from ecommerce_shop.models import Product

def home(request):
    products= Product.objects.all()
    allProds=[]
    catprods= Product.objects.values('category', 'id')
    cats= {item["category"] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params={'allProds':allProds }
    return render(request,'home.html', params)
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

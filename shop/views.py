from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()
    allProds=[]
    catprod=Product.objects.values('category','id')
    cats=set()
    for i in catprod:
        cats.add(i['category'])
    for cat in cats:
        prod=Product.objects.filter(category=cat)
        n=len(prod)
        if n%4==0:
            nSlides=n//4
        else:
            nSlides=n//4+1
        allProds.append([prod,range(1,nSlides),nSlides])
    # allProds=[[products,range(1,nSlides),nSlides],[products,range(1,nSlides),nSlides]]
    params={'allProds':allProds}
    # params={'product':products,'no_of_slides':nslides,'myrange':range(1,nslides) }
    return render(request,'shop/index.html',params)


def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return HttpResponse('we are at contact')
def tracker(request):
    return HttpResponse('we are at tracker')
def search(request):
    return HttpResponse('we are at search')
def productView(request):
    return HttpResponse('we are at productView')
def checkout(request):
    return HttpResponse('we are at contact')
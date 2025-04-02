from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Product
from math import ceil
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    allProds = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)
def about(request):
    return render(request,'shop/about.html')
def contact(request):
    return render(request,'shop/contact.html')
def tracker(request):
    return render(request,'shop/tracker.html')
def search(request):
    return render(request,'shop/search.html')
def productview(request, id):
    product = get_object_or_404(Product, product_id =id) # Change id to product_id
    print(product)
    return render(request, "shop/prodview.html", {"product": product})
def checkout(request):
    return render(request,'shop/checkout.html')

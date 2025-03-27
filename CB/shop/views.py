from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'shop/index.html')
def about(request):
    return HttpResponse("i am about")
def contact(request):
    return HttpResponse("i am contact")
def tracker(request):
    return HttpResponse("i am tracker")
def search(request):
    return HttpResponse("i am search")
def productview(request):
    return HttpResponse("i am productview")
def checkout(request):
    return HttpResponse("i am checkout")

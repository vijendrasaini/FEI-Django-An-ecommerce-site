from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'index.html',{})

def bodycare(request):
    result = Product.objects.all().filter(category = "bodycare")
    return render(request, "pages/body-care.html", {'products' : result})

def collections(request):
    result = Product.objects.all().filter(category = "collection")
    return render(request, "pages/collection.html", {'products' : result})

def makeup(request):
    return render(request, "pages/makeup.html", {})

def rituals(request):
    result = Product.objects.all().filter(category = "rituals")
    return render(request, "pages/rituals.html", {'products' : result})

def discover(request):
    return render(request, "pages/discover.html", {})

def signup(request):
    return render(request, "pages/signup.html", {})

def signin(request):
    return render(request, "pages/signin.html", {})

def wishlist(request):
    return render(request, "pages/wishlist.html", {})

def cart(request):
    return render(request, "pages/cart.html", {})

def paymentgateway(request):
    return render(request, "pages/paymentgateway.html", {})
    
def product(request):
    return render(request, "pages/productDetails.html", {})


from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserCustomForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.shortcuts import render
from .models import Product, Cart


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
    return render(request, "pages/discover.html")





def signup(request):
    if request.method == 'POST' :
        form = UserCustomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created successfully.")
            return HttpResponseRedirect('/signin')
    else:
        form = UserCustomForm()
    return render(request, "pages/signup.html", { 'form' : form})

def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "You are successfullly Logged In.")
                return HttpResponseRedirect('/')
    else :
        form = AuthenticationForm()
    return render(request, "pages/signin.html", { 'form' : form})

def user_logout(request):
    logout(request)
    messages.success(request, "You are successfully logged out.")
    return HttpResponseRedirect('/')









def wishlist(request):
    return render(request, "pages/wishlist.html", {})

def cart(request):
    print("HI at cart")
    try:
        if request.user.is_authenticated:
            cart_list = Cart.objects.all().filter(user_id=request.user.id)
            product_list = Product.objects.all()
            products = []
            price_total = 0
            for cart_item in cart_list:
                for product in product_list:
                    if product.id == cart_item.product_id:
                        products.append({
                            'id' : product.id,
                            'cart_id' : cart_item.id,
                            'image' : product.image,
                            'price' : product.price,
                            'qty' : cart_item.product_qty,
                            'name' : product.name
                        })
                        final_price = 0
                        if product.price[0] == '₹':
                            price_str = product.price.split('₹')
                            final_price = float(price_str[1]) * cart_item.product_qty
                        else:
                            final_price = float(product.price) * cart_item.product_qty
                        price_total = price_total + final_price
            return render(request, "pages/cart.html", {'products' : products, 'total_products' : len(products), 'totol_price' : price_total})
        else:
            return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

def add_to_cart(request, id):
    try:
        if request.user.is_authenticated:
            product_id = id
            user_id = request.user.id
            cart_items = Cart.objects.all()
            flag = 1
            print(product_id, user_id)
            for cart_item in cart_items:
                if cart_item.product_id == int(id) and cart_item.user_id == int(user_id):
                    cart_item.product_qty = cart_item.product_qty + 1
                    cart_item.save()
                    print('inside loop and matched')
                    flag = 0
                    break
            if flag == 1:
                print("not foutn fitst product is cart")
                added_product = Cart(user_id=user_id, product_id=product_id)
                added_product.save()  
            messages.success(request, 'Product is added into your cart successfully.')
            return HttpResponseRedirect('/bodycare')
        else:
            messages.error(request, "please login to add the product into card.")
            return HttpResponseRedirect('/bodycare')
    except:
        messages.error(request, "product is not added.Something wrong has happpened")
        return HttpResponseRedirect('/bodycare')

def qtychange(request, product_id, qty_change):
    if request.user.is_authenticated : 
        user_id = request.user.id
        product = Cart.objects.get(user_id=user_id, product_id=product_id)
        if product.product_qty == 1 and int(qty_change) == -1:
            product.delete()
        else:
            product.product_qty = product.product_qty + int(qty_change)
            product.save()
    return HttpResponseRedirect('/cart')

def delete_from_cart(request, cart_id):
    if request.user.is_authenticated : 
        product = Cart.objects.get(id=cart_id)
        print(product)
        product.delete()
    return HttpResponseRedirect('/cart')













def paymentgateway(request):
    return render(request, "pages/paymentgateway.html", {})
    
def product(request, id):
    result = Product.objects.get(pk=id)
    return render(request, "pages/productDetails.html", {'product' : result})

def addtowishlist(request, id):
    result = Product.objects.get(pk=id)
    return render(request, "pages/productDetails.html", {'product' : result})



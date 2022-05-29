from .models import Cart, Product

def is_authenticated(request):
    context = { 'is_authenticated' : request.user.is_authenticated}
    return context


def user_first_name(request):
    try:
        request.user.first_name
        context = { 'user_first_name' : request.user.first_name}
        return context
    except:
        return { 'user_first_name' : "NA"}


def cart_item_count(request):
    c = 0
    if request.user.is_authenticated:
        cart_list = Cart.objects.all().filter(user_id=request.user.id)
        product_list = Product.objects.all()
        for cart_item in cart_list:
            for product in product_list:
                if product.id == cart_item.product_id:
                    c = c + 1
    return { 'cart_item_count' :c }

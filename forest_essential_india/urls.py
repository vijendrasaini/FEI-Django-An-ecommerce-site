from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home' ),
    path('bodycare', views.bodycare, name='bodycare' ),
    path('makeup', views.makeup, name='makeup' ),
    path('rituals', views.rituals, name='rituals' ),
    path('collections', views.collections, name='collections' ),
    path('discover', views.discover, name='discover' ),
    path('signup', views.signup, name='signup' ),
    path('signin', views.signin, name='signin' ),
    path('wishlist', views.wishlist, name='wishlist' ),
    path('cart', views.cart, name='cart' ),
    path('paymentgateway', views.paymentgateway, name='paymentgateway' ),
    path('product/<id>', views.product, name='product' ),
    path('addtowishlist/<id>', views.addtowishlist, name='addtowishlist' ),
]
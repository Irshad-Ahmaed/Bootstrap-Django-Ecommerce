from django.urls import path
from . import views

from store.AuthController import authview, cart, wishlist, checkout

urlpatterns = [
    path('', views.HOME, name='home'),
    path('collections', views.Collections, name='collections'),
    path('collections/<str:slug>', views.CollectionsView, name='collectionsView'),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productView, name='productView'),

    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutPage, name='logoutPage'),

    path('add-to-cart', cart.addToCart, name='addToCart'),
    path('cart', cart.viewCart, name='cart'),
    path('update-cart', cart.updateCart, name='updateCart'),
    path('delete-cart-item', cart.deleteCartItem, name='deleteCartItem'),

    path('Wishlist', wishlist.index, name='wishlist'),
    path('add-to-wishlist', wishlist.addToWishlist, name='addToWishlist'),
    path('delete-wishlist-item', wishlist.deleteWishListItem, name='deletewishlistitem'),

    path('checkout', checkout.index, name='checkout'),
]
from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from store.models import Wishlist, Product

@login_required(login_url='loginpage')
def index(request):
    wishItems = Wishlist.objects.filter(user = request.user)
    context ={
        'wishItems': wishItems
    }
    return render(request, 'store/wishlist.html', context)

def addToWishlist(request):
    if request.method == 'POST':
        if (request.user.is_authenticated):
            prod_id = int(request.POST.get('product_id'))
            product_check= Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user=request.user, product_id = prod_id)):
                    return JsonResponse({'status': "Product already in wishlist"})
                else:
                    Wishlist.objects.create(user=request.user, product_id=prod_id)
                    return JsonResponse({'status': "Product added to wishlist"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')

def deleteWishListItem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            if(Wishlist.objects.filter(user=request.user, product_id = prod_id)):
                    wishlistItem = Wishlist.objects.get(product_id=prod_id)
                    wishlistItem.delete()
                    return JsonResponse({'status': "Product removed from wishlist"})
            else:
                return JsonResponse({'status': "Product Not found in wishlist"})
           
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('/')

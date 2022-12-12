from django.shortcuts import render
from .models import Product

# Create your views here.


def all_products(request):
    # A view to return all products including sorting and search queries page
    products = Product.objects.all()
    context ={
        'products': products,
    }
    return render(request, 'products/products.html', context)
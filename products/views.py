from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import ProductForm
from .models import Product

# Create your views here.


def all_products(request):
    # A view to return all products including sorting and search queries page
    products = Product.objects.all()
    context ={
        'products': products,
    }
    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    # A view to show individual product details 

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
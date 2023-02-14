from django.shortcuts import render, get_object_or_404
from .models import Review
from products.models import Product


# Create your views here.


def product_detail_review(request, product_id):
    # A view to return index page
    product = get_object_or_404(Product, pk=product_id)
    reviews = Review.objects.filter(product=product)
    return render(request, 'reviews/product_detail_review.html', {'product': product, 'reviews': reviews})
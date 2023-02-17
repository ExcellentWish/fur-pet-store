from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Review
from .forms import ReviewForm
from django.views import generic, View
from products.models import Product


# Create your views here.


class ProductDetailReview(View):
    def get(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        reviews = Review.objects.filter(product=product, approved=True).order_by("-created_date")
        template = 'reviews/product_detail_review.html'
        liked = False
        for review in reviews:
            if review.likes.filter(id=self.request.user.id).exists():
                liked = True

        return render(request,
            template,
            {
                "product": product,
                "reviews": reviews,
                "liked": liked,
                "reviewed": False,
                "form": ReviewForm()
             },
        )

    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        reviews = Review.objects.filter(product=product, approved=True).order_by("-created_date")
        liked = False
        for review in reviews:
            if review.likes.filter(id=self.request.user.id).exists():
                liked = True

        form = ReviewForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.product = product
            review = form.save(commit=False)
            Review.objects.filter(user_id=3).delete()
            review = form.save()
            
        else:
            form = ReviewForm()
        
        return render(
            request,
            "reviews/product_detail_review.html",
            {
                "product": product,
                "reviews": reviews,
                "liked": liked,
                "reviewed": True,
                "form": form
            },
        )

class ReviewLike(View):
    
    def post(self, request, like, *args, **kwargs):
        review = get_object_or_404(Review, pk=like)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse("reviews/product_detail_review.html", args=[review.product.pk]))

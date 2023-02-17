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
        reviews = Review.objects.filter(product=product)
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
        reviews = Review.objects.filter(product=product)
        liked = False
        for review in reviews:
            if review.likes.filter(id=self.request.user.id).exists():
                liked = True
                

        return render(
            request,
            "reviews/product_detail_review.html",
            {
                "product": product,
                "reviews": reviews,
                "liked": liked,
                "reviewed": True,
                "form": ReviewForm()
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

@login_required
def add_review(request, product_id):
    """
    view to add reviews to the db
    """
    # checks if user has permition to add products
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('products'))

    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        print(product)        
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.instance.posted_by = request.user
            form.instance.product = product
            form.save()
            messages.success(request, 'review Added')
            return redirect(reverse('products',))
        else:
            messages.error(
                request,
                'The review was not added. Please check the form is valid.'
            )
    else:
        form = ReviewForm()

    template = "reviews/product_detail_review.html"
    context = {
        'form': form,
    }

    return render(request, template, context)


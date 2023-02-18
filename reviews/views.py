from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
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

        return render(request, template, {
                "product": product,
                'reviews': reviews,
                "liked": liked,
                "reviewed": False,
                "form": ReviewForm(),      
             },
        )

    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        reviews = Review.objects.filter(product=product, approved=True).order_by("-created_date")
        liked = False
        for review in reviews:
            if review.likes.filter(id=self.request.user.id).exists():
                liked = True

        # Create a new instance of the ReviewForm using the POST data
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and associate it with the current user and product
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return HttpResponseRedirect(reverse('product_detail_review', args=[product_id]))
        
        # If the form is not valid, return to the template with the errors and the original form data
        return render(
            request,
            "reviews/product_detail_review.html",
            {
                "product": product,
                'reviews': reviews,
                "reviews": reviews,
                "liked": liked,
                "reviewed": True,
                "form": form,
            },
        )

class EditReview(View):
    def get(self, request, review_id, *args, **kwargs):
        # Get the review object to edit
        review = get_object_or_404(Review, pk=review_id)

        # checks if user has permission to edit there review
        if request.user != review.posted_by:
            messages.error(request, 'Sorry, only the user the created this review can do that.')
            return redirect(reverse('product_detail_review'))
        
        template = 'reviews/edit_review.html'
        form = ReviewForm(instance=review)

        return render(request,
            template,
            {
                "product": review.product,
                "review": review,
                "form": form,
             },
        )

    def post(self, request, review_id, *args, **kwargs):
        # Get the review to edit
        review = get_object_or_404(Review, pk=review_id)

        if request.user != review.user:
            messages.error(request, 'Sorry, only the user who created this review can edit it.')
            return redirect(reverse('product_detail_review', args=[review.product.id]))

        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            # Save the edited review
            edited_review = form.save()            
            # Redirect to the product detail page
            return redirect(reverse('product_detail_review', args=[review.product.id]))
        
        return render(
            request,
            "reviews/edit_review.html",
            {
                'form': form,
                'review': review,
            },
        ) 
    


class DeleteReview(View):
    @login_required
    def delete_review(request, review_id):
        # View for user to delete review
        def get(self, request, review_id, *args, **kwargs):
            return render(request, "reviews/delete_review.html")   




class ReviewLike(View):
    
    def post(self, request, like, *args, **kwargs):
        review = get_object_or_404(Review, pk=like)
        if review.likes.filter(id=request.user.id).exists():
            review.likes.remove(request.user)
        else:
            review.likes.add(request.user)

        return HttpResponseRedirect(reverse("reviews/product_detail_review.html", args=[review.product.pk]))

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
        review = None
        if request.user.is_authenticated:
            try:
                review = Review.objects.get(product=product, user=request.user)
            except Review.DoesNotExist:
                pass
        reviews = Review.objects.filter(product=product, approved=True).order_by("-created_date")
        template = 'reviews/product_detail_review.html'
        reviewed = False
        if request.user.is_authenticated:
            try:
                Review.objects.get(product=product, user=request.user,)
                reviewed = True
            except Review.DoesNotExist:
                pass
                
        

        context = {
            "product": product,
            'reviews': reviews,
            "reviewed": reviewed,
            "form": ReviewForm(),
            "review": review,
        }

        return render(request, template, context)

    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        reviews = Review.objects.filter(product=product, approved=True).order_by("-created_date")
        review = None        
        # Create a new instance of the ReviewForm using the POST data
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form and associate it with the current user and product
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, 'You left a review. Please wait for approval')
            return HttpResponseRedirect(reverse('product_detail_review', args=[product_id]))
        
        # If the form is not valid, return to the template with the errors and the original form data
        context = {
            "product": product,
            'reviews': reviews,
            "reviewed": True,
            "form": form,
            'review': review,
        }
        
        return render(request, "reviews/product_detail_review.html", context)


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
            messages.success(request, 'Your review has been edited.')
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

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        # Check if the current user has permission to delete the review
        if request.user != review.user:
            messages.error(request, 'Sorry, only the user who created this review can delete it.')
            return redirect(reverse('product_detail_review', args=[review.product.id]))

        context = {'review': review}

        return render(request, 'reviews/delete_review.html', context)

    def post(self, request, review_id):
        # Get the review to delete
        review = get_object_or_404(Review, pk=review_id)
        # Delete the review
        review.delete()
        messages.success(request, 'Your review has been deleted.')
        # Redirect to the product detail page
        return redirect(reverse('product_detail_review', args=[review.product.id])) 

def like_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user in review.likes.all():
        review.likes.remove(request.user)
    else:
        review.likes.add(request.user)
    return redirect('product_detail_review', product_id=review.product.id)

def dislike_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    if request.user in review.dislikes.all():
        review.dislikes.remove(request.user)
    else:
        review.dislikes.add(request.user)
        if request.user in review.likes.all():
            review.likes.remove(request.user)
    return redirect('product_detail_review', product_id=review.product.id)
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
        try:
            review = Review.objects.get(product=product)
        except Review.DoesNotExist:
            review = None
        reviews = Review.objects.filter(product=product, approved=True).order_by("-created_date")
        template = 'reviews/product_detail_review.html'
        liked = False
        disliked = False
        reviewed = False
        if request.user.is_authenticated:
            try:
                Review.objects.get(product=product, user=request.user)
                reviewed = True
            except Review.DoesNotExist:
                pass
                
        for review in reviews:
            if review.likes.filter(id=request.user.pk).exists():
                liked = True
            if review.dislikes.filter(id=request.user.pk).exists():
                disliked = True

        return render(request, template, {
                "product": product,
                'reviews': reviews,
                "liked": liked,
                "disliked": disliked,
                "reviewed": reviewed,
                "form": ReviewForm(),
                "review": review,
             },
        )

    def post(self, request, product_id, *args, **kwargs):
        product = get_object_or_404(Product, pk=product_id)
        reviews = Review.objects.filter(product=product, approved=True).order_by("-created_date")
        liked = False
        disliked = False
        for review in reviews:
            if review.likes.filter(id=request.user.pk).exists():
                liked = True
            if review.dislikes.filter(id=request.user.pk).exists():
                disliked = True 
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
        return render(
            request,
            "reviews/product_detail_review.html",
            {
                "product": product,
                'reviews': reviews,
                "reviews": reviews,
                "liked": liked,
                "disliked": disliked,
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



class ReviewLikeDislike(View):
    def post(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        user = request.user
        if 'like' in request.POST:
            if user in review.likes.all():
                review.likes.remove(user)
            else:
                review.likes.add(user)
                review.dislikes.remove(user)
        elif 'dislike' in request.POST:
            if user in review.dislikes.all():
                review.dislikes.remove(user)
            else:
                review.dislikes.add(user)
                review.likes.remove(user)
        product = review.product
        return redirect(reverse('product_detail_review', kwargs={'product_id': product.pk}))

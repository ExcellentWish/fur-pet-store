from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import UserProfile, UserWishlist
from .forms import UserProfileForm
from products.models import Product

# Create your views here.


def profile(request):
    # display the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your profile has been updated successfully'
            )
        else:
            messages.error(
                request,
                'Update failed. Please make sure the information is valid.'
            )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
        'not_shopping': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'not_shopping': True
    }

    return render(request, template, context)


def user_wishlist(request):
    """ display wishlist """
    if request.user.is_authenticated:
        return render(request, 'profiles/wishlist.html')
    else:
        messages.error(request, "You must be logged in to view a wishlist.")
        return redirect('home')


def add_to_wishlist(request, item_id):
    """ view to display orders to user """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        product = get_object_or_404(Product, pk=item_id)
        if UserWishlist.objects.filter(user=user, product=product).exists():
            wishlist_item = UserWishlist.objects.get(
                user=user,
                product=product
            )
            wishlist_item.delete()
            messages.info(request, "removed from wishlist")
            return redirect('products')
        else:
            wishlist_item = UserWishlist.objects.create(
                user=user,
                product=product
            )
            messages.success(request, f"{wishlist_item} added to wishlist")
            return redirect(reverse('products'))
    else:
        messages.error(request, "You must be logged in to create a wishlist.")
        return redirect(reverse('products'))


def remove_from_wishlist(request, item_id):
    """ view to display orders to user """
    # if user is authenticated
    if request.user.is_authenticated:
        # get user instance
        user = UserProfile.objects.get(user=request.user)
        # get product using pk
        product = get_object_or_404(Product, pk=item_id)
        # get wishlist item using user & product
        wishlist_item = UserWishlist.objects.get(user=user, product=product)
        # delete item from wishlist
        wishlist_item.delete()
        messages.info(request, f"{product.name} removed from wishlist")
        return redirect(reverse('wishlist'), kwargs={'not_shopping': True})
    else:
        # if not logged in redirect back to all products
        messages.error(request, "You must be logged in to edit a wishlist.")
        return redirect(reverse('all_products'), kwargs={'not_shopping': True})

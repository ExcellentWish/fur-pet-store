from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile, UserWishlist
from .forms import UserProfileForm

# Create your views here.



def profile(request):
    # display the user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully')
        else:
            messages.error(request, 'Update failed. Please make sure the information is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True,
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
    }

    return render(request, template, context)

def user_wishlist(request):
    """ display wishlist """
    if request.user.is_authenticated:
        user = UserProfile.objects.get(user=request.user)
        list_to_display = []
        for item in UserWishlist.objects.filter(user=user):
            list_to_display.append(item.product)
        print(list_to_display)
        # products = Product.objects.filter(product_wishlist=request.user)
        context = {
            'wishlist_items': list_to_display,
        }
        return render(request, 'profiles/wishlist.html', context)
    else:
        messages.error(request, "You must be logged in to view a wishlist.")
        return redirect('home')

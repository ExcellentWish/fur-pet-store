from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    color = None
    
    if 'product_size' in request.POST:
        size = request.POST['product_size']

    if 'product_color' in request.POST:
        color = request.POST['product_color']

    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                if color:
                    if color in bag[item_id]['items_by_size'][size]['items_by_color'].keys():
                        bag[item_id]['items_by_size'][size]['items_by_color'][color] += quantity
                        messages.success(request, f'Updated {color.upper()} size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]["items_by_color"][color]}')
                    else:
                        bag[item_id]['items_by_size'][size]['items_by_color'][color] = quantity
                        messages.success(request, f'Added {color.upper()} size {size.upper()} {product.name} to your bag')
                else:
                    bag[item_id]['items_by_size'][size] += quantity
                    messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                if color:
                    bag[item_id]['items_by_size'][size] = {'items_by_color': {color: quantity}}
                    messages.success(request, f'Added {color.upper()} size {size.upper()} {product.name} to your bag')
                else:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
        else:
            if color:
                bag[item_id] = {'items_by_size': {size: {'items_by_color': {color: quantity}}}}
                messages.success(request, f'Added {color.upper()} size {size.upper()} {product.name} to your bag')
            else:
                bag[item_id] = {'items_by_size': {size: quantity}}
                messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    else:
        if item_id in list(bag.keys()):
            if color:
                if 'items_by_color' in bag[item_id].keys():
                    if color in bag[item_id]['items_by_color'].keys():
                        bag[item_id]['items_by_color'][color] += quantity
                        messages.success(request, f'Updated {color.upper()} {product.name} quantity to {bag[item_id]["items_by_color"][color]}')
                    else:
                        bag[item_id]['items_by_color'][color] = quantity
                        messages.success(request, f'Added {color.upper()} {product.name} to your bag')
                else:
                    bag[item_id]['items_by_color'] = {color: quantity}
                    messages.success(request, f'Added {color.upper()} {product.name} to your bag')
            else:
                bag[item_id] += quantity
                messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            if color:
                bag[item_id] = {'items_by_color': {color: quantity}}
                messages.success(request, f'Added {color.upper()} {product.name} to your bag')
            else:
                bag[item_id] = quantity
                messages.success(request, f'Added {product.name} to your bag')
    request.session['bag'] = bag
    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    quantity = int(request.POST.get('quantity'))
    size = None
    color = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    if 'product_color' in request.POST:
        color = request.POST['product_color']
    bag = request.session.get('bag', {})

    if size and color:
        if quantity > 0:
            bag[item_id]['items_by_size'][size]['items_by_color'][color] = quantity
        else:
            del bag[item_id]['items_by_size'][size]['items_by_color'][color]
            if not bag[item_id]['items_by_size'][size]['items_by_color']:
                bag[item_id]['items_by_size'].pop(size)
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    elif size:
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
    elif color:
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        size = None
        color = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        if 'product_color' in request.POST:
            color = request.POST['product_color']
        bag = request.session.get('bag', {})

        if size and color:
            del bag[item_id]['items_by_size'][size]['items_by_color'][color]
            if not bag[item_id]['items_by_size'][size]['items_by_color']:
                bag[item_id]['items_by_size'].pop(size)
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        elif size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        elif color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)

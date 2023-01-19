from django.shortcuts import render

# Create your views here.

def index(request):
    # A view to return index page
    return render(request, 'home/index.html')

def about(request):
    """ A view to return the about page """
    return render(request, 'home/about.html')

def privacy_policy(request):
    """ A view to return the about page """
    return render(request, 'home/privacy_policy.html')


def terms_conditions(request):
    """ A view to return the about page """
    return render(request, 'home/terms_conditions.html')

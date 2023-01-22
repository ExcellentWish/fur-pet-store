from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.



def profile(request):
    # display the user's profile
    template = 'profiles/profile.html'
    context = {
        'profile': profile,
    }

    return render(request, template, context)

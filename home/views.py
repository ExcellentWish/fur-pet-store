from django.shortcuts import render
from django.views import generic, View
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

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

def send_message(request, contact_form):
    # Function to send email after contact form submitted
    customer_name = contact_form.cleaned_data['name']
    email_from = contact_form.cleaned_data['email']
    subject = (f'Message from {customer_name}, {email_from}')
    message = contact_form.cleaned_data['message']
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, email_from, recipient_list)

class ContactPage(View):

    def get(self, request, *args, **kwargs):
        contact_form = ContactForm()
        template = 'home/contact_us.html'
        return render(request, template, {'contact_form': contact_form})


    def contact_form(request):

        if request.method == 'POST':
            contact_form = ContactForm(request.POST)

            if form.is_valid():
                return render(request, 'home/contact_us.html', {'contact_form': contact_form})

            else:
                contact_form = ContactForm()

            return render(request, 'home/contact_us.html', {'contact_form': contact_form})

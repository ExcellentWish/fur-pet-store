from django.shortcuts import render
from django.views import generic, View
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from fur_pet_store.views import handler404, handler500
from profiles.models import UserProfile

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
        


def get_customer_instance(request, User):
    # Returns customer instance if User is logged in
    customer_email = request.user.email
    customer = UserProfile.objects.filter(email=customer_email).first()
    return customer


class ContactPage(View):

    def get(self, request, *args, **kwargs):

        contact_form = ContactForm()
        template = 'home/contact_us.html'
        if request.user.is_authenticated:
            # if user is logged in pre-populate the fields
            contact_form = ContactForm(
                initial={
                    'name': request.user.first_name + " " + request.user.last_name,
                    'email': request.user.email
                }
            )

        else:
            contact_form = ContactForm()
        return render(request, template, {'contact_form': contact_form})

    def post(self, request, User=User, *args, **kwargs):
        if request.method == 'POST':
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                # Return blank form so the same message isn't posted twice.
                send_message(request, contact_form)
                contact_form = ContactForm()
                messages.add_message(
                    request,
                    messages.SUCCESS,
                    "Thank you for contacting us,\
                    one of our staff will be in touch shortly."
                )
                return render(
                    request,
                    'home/contact_us.html',
                    {'contact_form': contact_form}
                )
            else:
                contact_form = ContactForm(request.POST)
                messages.add_message(
                    request,
                    messages.ERROR,
                    "Something is not right with your form -\
                    please make sure your email address\
                    is entered in the correct format."
                )

            return render(request, template, {'contact_form': contact_form})


from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('privacy_policy', views.privacy_policy, name='privacy_policy'),
    path('terms_conditions', views.terms_conditions, name='terms_conditions'),
    path('contact_us', views.ContactPage.as_view(), name='contact_us'),    
]

from django.contrib import admin
from .models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin):
    """ allows admin to view user profiles """
    model = UserProfile
    readonly_fields = ('user', 'full_name',)
    fields = ('user', 'full_name', 'default_email', 'phone_number',
              'default_street_address1', 'default_street_address2',
              'default_town_or_city', 'default_postcode',
              'default_country')

    list_display = ('user', 'full_name', 'default_email')


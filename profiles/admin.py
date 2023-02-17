from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, UserWishlist
# Register your models here.


@admin.register(UserWishlist)
class WishlistAdmin(admin.ModelAdmin):
    model = UserWishlist
    fields = ('user', 'product')
    list_display = ('user', 'product')
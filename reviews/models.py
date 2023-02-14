from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rating = models.IntegerField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
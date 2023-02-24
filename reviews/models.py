from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    body = models.TextField()
    likes = models.ManyToManyField(User, blank=True, related_name='product_like')
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_added",
        null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    """will order class based on crrated on date.
        inspired by code institue blog walk through project """
    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

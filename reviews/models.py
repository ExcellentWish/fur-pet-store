from django.db import models
from django.contrib.auth.models import User
from profiles.models import UserProfile
from products.models import Product

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='review_likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='review_dislikes', blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return f"Comment {self.body} by {self.user}"

    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_dislikes(self):
        return self.dislikes.count()

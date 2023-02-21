from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.


class Review(models.Model):
    title = models.CharField(max_length=200)
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    body = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posted_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_added",
        null=True)
    likes = models.ManyToManyField(
        User,
        related_name='review_likes',
        blank=True
    )
    like_count = models.PositiveIntegerField(default=0)
    dislikes = models.ManyToManyField(
        User,
        related_name='review_dislikes',
        blank=True
    )
    dislike_count = models.PositiveIntegerField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    """will order class based on crrated on date.
        inspired by code institue blog walk through project """
    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title

    def __str__(self):
        return f"Comment {self.body} by {self.user}"

    def number_of_likes(self):
        return self.likes.count()

    def number_of_dislikes(self):
        return self.dislikes.count()

    def save(self, *args, **kwargs):
        self.like_count = self.likes.count()
        self.dislike_count = self.dislikes.count()
        super(Review, self).save(*args, **kwargs)

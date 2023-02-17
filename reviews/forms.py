from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """
    creates a form to add a new review for a product
    """
    class Meta:
        model = Review
        fields = ('title','body')

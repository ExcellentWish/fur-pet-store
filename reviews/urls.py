from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path(
        '<int:product_id>/',
        views.ProductDetailReview.as_view(), name='product_detail_review'),
    path(
        'edit/<int:review_id>/',
        views.EditReview.as_view(), name='edit_review'),
    path(
        'delete/<int:review_id>/',
        views.DeleteReview.as_view(), name='delete_review'),
    path(
        '<int:review_id>', views.like_review, name='like_review'),
    path(
        '<int:review_id>/dislike/',
        views.dislike_review, name='dislike_review'),
]

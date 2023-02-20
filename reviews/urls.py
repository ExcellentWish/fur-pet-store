from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path('<int:product_id>/', views.ProductDetailReview.as_view(), name='product_detail_review'),
    path('<int:pk>/like-dislike/', views.ReviewLikeDislike.as_view(), name='review_like_dislike'),
    path('edit/<int:review_id>', views.EditReview.as_view(), name='edit_review'),
    path('delete/<int:review_id>', views.DeleteReview.as_view(), name='delete_review'),
]

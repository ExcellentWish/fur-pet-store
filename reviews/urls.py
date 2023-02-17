from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path('<int:product_id>/', views.ProductDetailReview.as_view(), name='product_detail_review'),    
]

from django.urls import path, include, reverse
from . import views

urlpatterns = [
    path('<int:product_id>/', views.product_detail_review, name='product_detail_review')
]
# urls.py
from django.urls import path
from delivery.views import CalculatePrice

urlpatterns = [
    path('calculate-price/', CalculatePrice.as_view(), name='calculate_price'),
    # Other URL patterns for your project
]

from django.urls import path
from .api_views import product_api,details

urlpatterns = [
    path('prod/',product_api),
    path('prod/<int:id>/',details)
]
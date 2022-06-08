from django.urls import path
from cart.views import *


urlpatterns = [
    path('add/<int:product_id>', AddToCart.as_view()),
    path('', GetCart.as_view())

]

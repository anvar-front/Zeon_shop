from django.urls import path
from cart.views import *


urlpatterns = [
    path('add/<int:product_id>', AddToCart.as_view()),
    path('', GetCart.as_view()),
    path('remove/<int:pk>', CartRemove.as_view()),
    path('clear', ClearCart.as_view()),
    path('order', OrderAPIView.as_view())
]

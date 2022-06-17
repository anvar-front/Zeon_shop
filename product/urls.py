from django.urls import path
from product.views import *


urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('collection/', CollectionAPIView.as_view()),
    path('by_collection/', Product_by_collectionAPIView.as_view()),
    path('favorite/', Favorite_productAPIView.as_view()),
    path('bestseller/', Product_bestsellerAPIView.as_view()),
    path('new/', Product_newAPIView.as_view())
]

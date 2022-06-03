from django.urls import path
from rest_framework import routers
from product.views import *


# router = routers.DefaultRouter()
# router.register('collection', CollectionViewset),
# router.register('similarproduct', SimilarProductViewset),
# router.register('productbycollection', ProductByCollectionViewset)


# router.register('productlist', ProductViewset)

urlpatterns = [
    path('', ProductAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('collection/', CollectionAPIView.as_view()),
    path('by_collection/', Product_by_collectionAPIView.as_view()),
    path('new/', New_productAPIView.as_view()),
    path('favorite/', Favorite_productAPIView.as_view())


]
import random

from news.pagination import PaginationHandlerMixin
from rest_framework import filters, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .models import *
from .serializers import *


class CustomPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'limit'
    max_page_size = 50


class CollectionAPIView(APIView):

    def get(self, request, format=None):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)


class ProductAPIView(APIView):
    max_page_size = 12

    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'material', 'fabric_structure']


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = Product_itemSerializer(article)
        return Response(serializer.data)


class SimilarProductAPIView(APIView):

    def get(self, request, format=None):
        collection = Collection.objects.all()[:5]
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)


class Product_by_collectionAPIView(APIView, PaginationHandlerMixin):
    pagination_class = CustomPagination
    serializer_class = Product_by_collectionSerializer

    def get(self, request, format=None):
        collection = Collection.objects.all()[:12]
        page = self.paginate_queryset(collection)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
            serializer = self.serializer_class(collection, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class New_productAPIView(APIView):
    def get(self, request, format=None):
        new = Product.objects.filter(new = True)[:5]
        serializer = New_productsSerializer(new, many=True)
        return Response(serializer.data)


class Favorite_productAPIView(APIView, PaginationHandlerMixin):

    def get(self, request, format=None):

        qs = Product.objects.filter(favorite=True)
        if qs is not None:
            serializer = ProductSerializer(qs, many=True)
        else:
            queryset = set(Product.objects.values_list('collection', flat=True)[:5])
            res = [random.choice(Product.objects.filter(collection=i)) for i in queryset]
            serializer = ProductSerializer(res, many=True)
        return Response(serializer.data)

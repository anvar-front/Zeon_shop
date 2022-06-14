import random

from news.pagination import PaginationHandlerMixin
from rest_framework import filters, generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class CustomPagination(PageNumberPagination):
    """
    Класс для пагинации
    """
    page_size = 8
    page_size_query_param = 'limit'
    max_page_size = 50


class CollectionAPIView(APIView):
    """
    Представление для коллекции
    """
    def get(self, request, format=None):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)


class ProductAPIView(generics.ListAPIView, PaginationHandlerMixin):
    """
    Представление для продукта
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'material']

    """
    Функция для вывода товаров из 5 разных коллекций по одному. Если в поисковик не нашел определенный товар
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            queryset = set(Product.objects.values_list('collection', flat=True))
            queryset = [random.choice(Product.objects.filter(collection=i)) for i in queryset][:5]
            serializer = self.get_serializer(queryset, many=True)
            return Response({'answer': 'По вашему запросу ничего не найдено', 'Возможно вас интересует':serializer.data})

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    

class ProductDetailAPIView(APIView):
    """
    Представление для определенного (detail) товара
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = Product_itemSerializer(article)
        return Response(serializer.data)


class Product_by_collectionAPIView(APIView, PaginationHandlerMixin):
    """
    Поедставление для вывода продуктов по коллекциям
    """
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
    """
    Представление для новых продуктов
    """
    def get(self, request, format=None):
        new = Product.objects.filter(new = True)[:5]
        serializer = SecondProductSerializer(new, many=True)
        return Response(serializer.data)


class Favorite_productAPIView(APIView, PaginationHandlerMixin):
    """
    Представление для избранныз продуктов
    """
    def get(self, request, format=None):
        qs = list(Product.objects.filter(favorite=True))
        print(qs)
        print(True if len(qs) > 0 else False)
        if len(qs) > 0:
            serializer = ProductSerializer(qs, many=True)
            print("some")
        else:
            queryset = set(Product.objects.values_list('collection', flat=True))
            res = [random.choice(Product.objects.filter(collection=i)) for i in queryset]
            print(res)
            serializer = ProductSerializer(res, many=True)
        return Response(serializer.data)

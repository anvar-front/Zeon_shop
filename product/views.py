import random

from news.pagination import PaginationHandlerMixin
from rest_framework import filters, generics, permissions, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


class EightPagination(PageNumberPagination):
    """
    Класс для пагинации
    """
    page_size = 8
    page_size_query_param = 'limit'
    max_page_size = 50


class TwelvePagination(PageNumberPagination):
    """
    Класс для пагинации
    """
    page_size = 12
    page_size_query_param = 'limit'
    max_page_size = 50


class CollectionAPIView(APIView):
    """
    Представление для коллекции
    """
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, context={'request': request}, many=True)
        return Response(serializer.data)


class CollectionDetailAPIView(APIView):
    """
    Представление для вывода товаров выбранной коллекции
    """
    permission_classes = [permissions.AllowAny]
    pagination_class = TwelvePagination

    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        collection = self.get_object(pk)
        print(type(collection))
        serializer = Collection_detailSerializer(collection)
        new_poducts = Product.objects.filter(new=True)[:5]
        return Response({"Products": serializer.data, "New_products": (ProductSerializer(new_poducts, many=True).data)})


class ProductAPIView(generics.ListAPIView, PaginationHandlerMixin):
    """
    Представление для продукта
    """
    permission_classes = [permissions.AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = TwelvePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'material']

    """
    Функция для вывода товаров из 5 разных коллекций по одному.
    Если поисковик не нашел определенный товар
    """
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            queryset = set(Product.objects.values_list(
                'collection',
                flat=True
                ))
            queryset = [random.choice(Product.objects.filter(collection=i)) for i in queryset][:5]
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                'answer': 'По вашему запросу ничего не найдено',
                'Возможно вас интересует': serializer.data
                })

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
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = Product_itemSerializer(product)
        return Response(serializer.data)


class Favorite_productAPIView(APIView, PaginationHandlerMixin):
    """
    Представление для избранных продуктов
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        qs = Favorite.objects.filter(user=request.user)
        qs = [product.product for product in qs]
        if len(qs) > 0:
            serializer = ProductSerializer(qs, many=True)
            return Response({
                "Количество": len(qs),
                "Избранные товары": serializer.data})
        else:
            queryset = set(Product.objects.values_list('collection', flat=True))
            res = [random.choice(Product.objects.filter(collection=i)) for i in queryset]
            serializer = ProductSerializer(res, many=True)
            return Response({
                "Избранное": "У Вас пока нет избранных товаров",
                "Возможно Вас заинтересует": serializer.data
                })


class Favorite_ADD(APIView):
    """ 
    Представление для добавоения товара в избранные
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        Favorite(product_id=pk, user=request.user).save()
        return Response({"status": "added"})


class Favorite_REMOVE(APIView):
    """
    Представление для удаления товара из избранных
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk, format=None):
        Favorite.objects.filter(product_id=pk, user=request.user).delete()
        return Response({"status": "removed"})


class Product_bestsellerAPIView(APIView, PaginationHandlerMixin):
    """
    Для продуктов - хит продаж
    """
    pagination_class = EightPagination
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        bestseller = Product.objects.filter(bestseller=True)
        page = self.paginate_queryset(bestseller)
        if page is not None:
            serializer = self.get_paginated_response(
                ProductSerializer(page, many=True).data
                )
        else:
            serializer = ProductSerializer(bestseller, many=True)
        return Response(serializer.data)


class Product_newAPIView(APIView, PaginationHandlerMixin):
    """
    Для новых продуктов
    """
    pagination_class = EightPagination
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        new = Product.objects.filter(new=True)
        page = self.paginate_queryset(new)
        if page is not None:
            serializer = self.get_paginated_response(
                ProductSerializer(page, many=True).data
                )
        else:
            serializer = ProductSerializer(new, many=True)
        return Response(serializer.data)

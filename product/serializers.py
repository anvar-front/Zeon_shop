from rest_framework import serializers
from .models import *
from django.db.models import Q

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


class Image_colorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image_color
        fields = ['image', 'color']


class ProductSerializer(serializers.ModelSerializer):
    images = Image_colorSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'collection', 'vendor_code', 'price', 'discount', 'new_price', 'description', 'material', 'quantity', 'size_range', 'favorite', 'images']


# Сериализатор для вывода 5шт товаров из той же коллекции
class SimilarProductSerializer(serializers.ModelSerializer):
    images = Image_colorSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'new_price', 'size_range', 'favorite', 'images']


class Product_itemSerializer(serializers.ModelSerializer):
    similar = serializers.SerializerMethodField('similarity')
    images = Image_colorSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'collection', 'vendor_code', 'price', 'discount', 'new_price', 'description', 'material', 'quantity', 'size_range', 'favorite', 'images', 'similar']

    # Функция для вывода 5 похожих товаров и одной коллекции
    # Q - для искоючения самого обьекта из списка
    def similarity(self, obj):
        similar = Product.objects.filter(Q(collection = obj.collection)&~Q(id=obj.id))[:5]
        similar_data = SimilarProductSerializer(similar, many=True)
        return similar_data.data



# Сериализатор для тикета Коллекция(товары)
class Product_for_collectionSerializer(serializers.ModelSerializer):
    images = Image_colorSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'new_price', 'size_range', 'favorite', 'images']


class Product_by_collectionSerializer(serializers.ModelSerializer):
    products = Product_for_collectionSerializer(many=True)
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products']


# Сериализатор для новых товаров
class New_productsSerializer(serializers.ModelSerializer):
    images = Image_colorSerializer(many=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'new_price', 'size_range', 'favorite', 'images']


from django.db.models import Q
from rest_framework import serializers

from .models import *


class CollectionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Сериализатор для коллекции
    """

    url = serializers.HyperlinkedIdentityField(
        view_name='product:collection-detail',
        lookup_field='pk'
    )

    class Meta:
        model = Collection
        fields = ['id', 'url', 'image', 'title']



class Collection_detailSerializer(serializers.ModelSerializer):
    """
    Вывод товаров выбранной коллекции
    """
    products = serializers.SerializerMethodField('get_products')

    class Meta:
        model = Collection
        fields = ['id', 'title', 'image', 'products']

    def get_products(self, obj):
        product = Product.objects.filter(collection=obj.id)
        product_data = ProductSerializer(product, many=True)
        return product_data.data


class Image_colorSerializer(serializers.ModelSerializer):
    """
    Сериализатор для фотографии и цвета для продукта
    """
    class Meta:
        model = Image_color
        fields = ['image', 'color']


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продукта
    """
    images = Image_colorSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'collection',
                  'vendor_code',
                  'price',
                  'discount',
                  'new_price',
                  'description',
                  'fabric_structure',
                  'material',
                  'quantity',
                  'size_range',
                  'images'
                  ]


class SecondProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для вывода 5шт товаров из той же коллекции
    Сериализатор для тикета Коллекция(товары)
    Сериализатор для новых товаров
    """
    images = Image_colorSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'price',
                  'discount',
                  'new_price',
                  'size_range',
                  'images'
                  ]


class Product_itemSerializer(serializers.ModelSerializer):
    """
    Сериализатор для определенного товара
    (выводит еще 5 продуктов из этой же коллекции)
    """
    similar = serializers.SerializerMethodField('similarity')
    images = Image_colorSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'collection',
                  'vendor_code',
                  'price',
                  'discount',
                  'new_price',
                  'description',
                  'material',
                  'quantity',
                  'size_range',
                  'images',
                  'similar'
                  ]

    """
    Функция для вывода 5 похожих товаров и одной коллекции
    Q - для искоючения самого обьекта из списка
    """
    def similarity(self, obj):
        similar = Product.objects.filter(Q(collection=obj.collection) & ~ Q(id=obj.id))[:5]
        similar_data = SecondProductSerializer(similar, many=True)
        return similar_data.data

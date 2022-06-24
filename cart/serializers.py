from dataclasses import field
from rest_framework import serializers
from product.models import Image_color, Product
from .models import *


class CartProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для проуктов корзины
    """
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'new_price', 'size_range']


class CartSerializer(serializers.ModelSerializer):
    """
    Сериализатор для самой корзины
    """
    def get_product(self, obj):
        serializer = CartProductSerializer(obj.image_color,
                                           context=self.context)
        return serializer.data

    def get_quantity(self, obj):
        return self.context[str(obj.image_color.id)]['colors'][str(obj.id)]

    quantity = serializers.SerializerMethodField('get_quantity')
    product = serializers.SerializerMethodField('get_product')

    class Meta:
        model = Image_color
        fields = ['quantity', 'image', 'color', 'product']


class OrdersSerializer(serializers.Serializer):
    """
    Сериализатор для клиента (заполнение данными)
    """
    name = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    phone_number = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)


class Product_to_OrderSerializer(serializers.ModelSerializer):
    """
    Сериализатор для заказанных продуктов
    """
    class Meta:
        model = Product_to_Order
        fields = '__all__'


class Order_checkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чека заказа
    """
    product = Product_to_OrderSerializer(many=True)

    class Meta:
        model = Order_check
        fields = ['id',
                  'product',
                  'quantity_line',
                  'quantity',
                  'price',
                  'discount',
                  'final_price']


class ClientSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения историю заказов
    """
    order_check = Order_checkSerializer(many=True)

    class Meta:
        model = Client
        fields = ['id', 'date', 'phone_number', 'status', 'order_check']

from rest_framework import serializers
from product.models import Image_color, Product
from .models import *


class CartProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'new_price', 'size_range']


class CartSerializer(serializers.ModelSerializer):
    def get_product(self, obj):
        print(self.context, '-------------------------1--------------------')
        serializer = CartProductSerializer(obj.image_color, context=self.context)
        return serializer.data

    def get_quantity(self, obj):
        return self.context[str(obj.image_color.id)]['colors'][str(obj.id)]

    quantity = serializers.SerializerMethodField('get_quantity')
    product = serializers.SerializerMethodField('get_product')
    class Meta:
        model = Image_color
        fields = ['quantity', 'image', 'color', 'product']


class OrdersSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    first_name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=30)
    phone_number = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
from rest_framework import serializers
from product.models import Image_color, Product


class CartProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'discount', 'new_price', 'size_range']


class CartSerializer(serializers.ModelSerializer):

    def get_product(self, obj):
        serializer = CartProductSerializer(obj.image_color, context=self.context)
        return serializer.data

    def get_quantity(self, obj):
        return self.context[str(obj.image_color.id)]['colors'][str(obj.id)]

    quantity = serializers.SerializerMethodField('get_quantity')
    product = serializers.SerializerMethodField('get_product')
    class Meta:
        model = Image_color
        fields = ['quantity', 'image', 'color', 'product']

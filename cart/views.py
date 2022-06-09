from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView


from .cart import Cart
from product.models import Product, Image_color
from .serializers import CartSerializer


class AddToCart(APIView):

    def post(self, request, product_id, format=None):
        # создаем экземпляр класса cart, и передаем сессию клиента - request
        cart = Cart(request)
        # получаем продукт из базы - product_id
        product = get_object_or_404(Product, id=product_id)
        # получаем цвет из базы - из POST запроса
        """
        {
            "product_color": "#ffffff" - любой цвет
        }
        """
        color_object = request.data.get('product_color').upper()
        color = get_object_or_404(Image_color, color=color_object, image_color=product)

        # вызываем функцию add из cart.py        
        cart.add(product, color)
        print(cart.cart)

        return Response({"status" : "Успешно"})


class GetCart(APIView):

    def get(self, request, format=None):
        cart = Cart(request)

        # получаем все товары из корзины пользователя в виде обьектов
        products_cart = cart.get_cart_products()
        # products = products_cart['products']
        colors = products_cart['colors']

        serial = CartSerializer(colors, many=True, context = cart.cart)
        return Response(serial.data)


class CartRemove(APIView):

    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        try:
            color_object = request.data.get('product_color').upper()
        except AttributeError:
            return Response({"message": "product_color is required"})
        minus = request.data.get('minus')
        # получаем обьект цвета товара
        color = get_object_or_404(Image_color, color=color_object, image_color=product)
        cart.remove(color=color, minus=minus)
        return Response({"status": "success"})


class ClearCart(APIView):

    def get(self, request, format=None):
        cart = Cart(request)
        cart.clear()
        return Response({"status": "clear"})
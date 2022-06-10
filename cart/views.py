from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .cart import Cart
from product.models import Product, Image_color
from .serializers import CartSerializer


class AddToCart(APIView):
    """
    Добавление товара в корзину
    """
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

        return Response({"status" : "success"})


class GetCart(APIView):
    """
    Получение товара из корзины
    """
    def get(self, request, format=None):
        cart = Cart(request)

        # получаем все товары из корзины пользователя в виде обьектов
        products_cart = cart.get_cart_products()
        colors = products_cart['colors']

        product_serial = CartSerializer(colors, many=True, context = cart.cart)
        price = cart.get_total_price()
        order = {
            "quantity": cart.__len__(),
            "line_quantity": cart.get_total_quantity(),
            "total_price": price['price'],
            "discount_price": price['price'] - price['discount'],
            "final_price": price['discount']
            }

        return Response({"Cart": product_serial.data, "Order": order})


class CartRemove(APIView):
    """
    Удаление товара из корзины
    Если в теле запроса указать {minus: true} 
    """
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
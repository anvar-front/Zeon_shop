from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView

from .cart import Cart
from product.models import Product, Image_color
from .serializers import *
from .models import *


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


class OrderAPIView(CreateAPIView):

    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

    def post(self, request, *args, **kwargs):

        cart = Cart(request)

        name = request.data['name']
        first_name = request.data['first_name']
        email = request.data['email']
        phone_number = request.data['phone_number']
        country = request.data['country']
        city = request.data['city']
        order = Orders.objects.create(name=name, first_name=first_name, email=email, phone_number=phone_number, country=country, city=city)


        price = cart.get_total_price()
        check = Order_check.objects.create(
            client = order,
            quantity_line = cart.__len__(),
            quantity = cart.get_total_quantity(),
            price = price['price'],
            discount = price['price'] - price['discount'],
            final_price = price['discount']
        )


        for key, item in cart.cart.items():
            print(item, '---------------------')
            for id, color in item['colors'].items():
                # print(item['price'], '------------------------------')
                image = Image_color.objects.get(id=int(id))
                price = item['price']
                new_price = item['new_price']
                quantity = color
                Product_to_Order.objects.create(client=check, 
                                                price=price, 
                                                new_price=new_price, 
                                                quantity=quantity, 
                                                image=image.image, 
                                                color=image.color, 
                                                name=image.image_color.name, 
                                                size_range=image.image_color.size_range
                                                )

        cart.clear()
        return Response(self.serializer_class(order).data)

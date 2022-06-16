from decimal import Decimal
from django.conf import settings
from product.models import Product, Image_color


class Cart(object):
    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, color, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {
                                    'colors': {str(color.id): 0},
                                    'old_price': str(product.price),
                                    'new_price': str(product.new_price),
                                    'quantity': 0,
                                    'price': str(product.price),
                                    'line_quantity': str(product.quantity)
                                    }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            try:
                self.cart[product_id]['colors'][str(color.id)] += 1
            except KeyError:
                self.cart[product_id]['colors'][str(color.id)] = quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, color, minus):
        """
        Удаление товара из корзины.
        """
        product_id = str(color.image_color.id)
        if product_id in self.cart:
            if not minus or self.cart[product_id]['colors'][str(color.id)] < 2:
                del self.cart[product_id]['colors'][str(color.id)]
                if self.cart[product_id]['colors'] == {}:
                    del self.cart[product_id]
            else: 
                self.cart[product_id]['colors'][str(color.id)] -= 1
                self.cart[product_id]['quantity'] -= 1
            self.save()

    def get_cart_products(self):
        """
        Получение товаров из корзины
        """
        product_ids = self.cart.keys()

        # получаем все цвета товара из корзины
        list_color = [list(color['colors'].keys()) for color in self.cart.values()]
        list_color_normal = set().union(*list_color)

        # получаем все товары из корзины
        product_list = Product.objects.filter(id__in=product_ids)

        # получаем все цвета полученных продуктов
        color_list = Image_color.objects.filter(id__in = list_color_normal)
        # color_list = [Image_color.objects.get()]
        return {"products": product_list, "colors": color_list}

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return {"price": sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values()),
                "discount": sum(Decimal(item['new_price']) * item['quantity'] for item in self.cart.values())}
        
    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_quantity(self):
        """
        Подсчет всех товаров из корзины (штук)
        """
        return sum(int(item['line_quantity']) * item['quantity'] for item in self.cart.values())


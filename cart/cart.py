from decimal import Decimal
from django.conf import settings
from product.models import Product, Image_color


class Cart(object):
    def __init__(self, request):
        """
        Инициализируем корзину
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            """
            Сохраняем пустую корзину в сессиях
            """
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, color, quantity=1, update_quantity=False):
        """
        Добавить продукт в корзину или обновить его количество.
        """
        product_id = str(product.id)
        
        if product_id not in self.cart:
            self.cart[product_id] = {
                                    'colors': {color: 0},
                                    'discount': str(product.new_price),
                                    'old_price': str(product.price),
                                    'new_price': str(product.new_price),
                                    'quantity': 0,
                                    'price': str(product.price)
                                    }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
            try:
                self.cart[product_id]['colors'][color] += 1
            except KeyError:
                self.cart[product_id]['colors'][color] = quantity
        self.save()

    def save(self):
        # Обновление сессии cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # Отметить сеанс как "измененный", чтобы убедиться, что он сохранен
        self.session.modified = True

    def remove(self, product):
        """
        Удаление товара из корзины.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Перебор элементов в корзине и получение продуктов из базы данных.
        """
        product_ids = self.cart.keys()
        # получение объектов product и добавление их в корзину
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['new_price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Подсчет всех товаров в корзине.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        """
        Подсчет стоимости товаров в корзине.
        """
        return (
            {"price": sum(Decimal(item['price']) * item['colors'].values() for item in self.cart.values())},
            {"discount": sum(Decimal(item['new_price']) * item['colors'].values() for item in self.cart.values())}
        )

    def get_cart_products(self):

        product_ids = self.cart.keys()

        # получаем все цвета товара из корзины
        list_color = [list(color['colors'].keys()) for color in self.cart.values()]
        list_color_normal = set().union(*list_color)

        # получаем все товары из корзины
        product_list = Product.objects.filter(id__in=product_ids)

        # получаем все цвета полученных продуктов
        color_list = Image_color.objects.filter(color__in = list_color_normal, image_color__in = product_list)

        return {"products": product_list, "colors": color_list}

        

    def clear(self):
        # удаление корзины из сессии
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
from django.contrib import admin
from django.contrib.admin import StackedInline, TabularInline
from django.utils.safestring import mark_safe
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import Client, Order_check, Product_to_Order


class Product_to_OrderInline(SuperInlineModelAdmin, TabularInline):
    model = Product_to_Order
    extra = 0
    readonly_fields = ('client',
                       'product_image_tag',
                       'product_color_tag',
                       'name',
                       'size_range',
                       'price',
                       'new_price',
                       'quantity')
    fields = ('client',
              'product_image_tag',
              'product_color_tag',
              'name', 'size_range',
              'price',
              'new_price',
              'quantity')
    can_delete = False

    def product_image_tag(self, obj):
        """Отображение картинки в админ панели"""
        return mark_safe(
            '<img src="%s" width="150" height="150" />' % (obj.image.url)
            )

    def product_color_tag(self, obj):
        """Отображение цвета в админ панели"""
        return mark_safe(
            '<img style="background-color:%s" width="150" height="30" />'
            % (obj.color)
            )

    product_image_tag.short_description = 'Фотография'
    product_color_tag.short_description = 'Цвет'


class OrderInline(SuperInlineModelAdmin, StackedInline):
    model = Order_check
    inlines = (Product_to_OrderInline,)
    extra = 0
    readonly_fields = ('client',
                       'quantity_line',
                       'quantity',
                       'price',
                       'discount',
                       'final_price')
    can_delete = False


class ClientAdmin(SuperModelAdmin):
    model = Client
    inlines = [OrderInline]
    readonly_fields = ('user',
                       'name',
                       'first_name',
                       'email',
                       'phone_number',
                       'country',
                       'city',
                       'date')
    list_display = ('get_fio',
                    'email',
                    'phone_number',
                    'country',
                    'city',
                    'get_total_price')

    def get_total_price(self, obj):
        order_check = Order_check.objects.get(client=obj)
        return order_check.final_price

    def get_fio(self, obj):
        return f"{obj.name} {obj.first_name}"

    get_fio.short_description = 'ФИО'
    get_total_price.short_description = 'Чек'


admin.site.register(Client, ClientAdmin)

from django.contrib import admin
from django.contrib.admin import TabularInline, StackedInline
from super_inlines.admin import SuperInlineModelAdmin, SuperModelAdmin

from .models import Orders, Product_to_Order, Order_check


class Product_to_OrderInline(SuperInlineModelAdmin, TabularInline):
    model = Product_to_Order
    extra = 0
    readonly_fields = ('client', 'image', 'color', 'name', 'size_range', 'price', 'new_price', 'quantity')
    can_delete = False


class OrderInline(SuperInlineModelAdmin, StackedInline):
    model = Order_check
    inlines = (Product_to_OrderInline,)
    extra = 0
    readonly_fields = ('client', 'quantity_line', 'quantity', 'price', 'discount', 'final_price')
    can_delete = False


class OrderAdmin(SuperModelAdmin):
    model = Orders
    inlines = [OrderInline]
    readonly_fields = ('name', 'first_name', 'email', 'phone_number', 'country', 'city')
    list_display = ('get_fio', 'email', 'phone_number', 'country', 'city', 'get_total_price')

    def get_total_price(self, obj):
        order_check = Order_check.objects.get(client=obj)
        return order_check.final_price

    def get_fio(self, obj):
        return f"{obj.name} {obj.first_name}"

    get_fio.short_description = 'ФИО'
    get_total_price.short_description = 'Чек'


admin.site.register(Orders, OrderAdmin)

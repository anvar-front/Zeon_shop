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


admin.site.register(Orders, OrderAdmin)

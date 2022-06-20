from django.contrib import admin
from .models import *


class ProductImgColor(admin.TabularInline):
    model = Image_color
    extra = 0
    max_num = 8
    min_num = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgColor]
    list_filter = ('collection',)
    list_display = ['id',
                    'collection',
                    'name',
                    'price',
                    'discount',
                    'new_price',
                    'size_range',
                    'quantity',
                    'bestseller',
                    'new']
    readonly_fields = ('quantity', 'new_price')
    fields = ('collection',
              'name',
              'price',
              'discount',
              'new_price',
              'description',
              'size_range',
              'quantity',
              'bestseller',
              'new')


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)

from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class ProductImgColor(admin.TabularInline):
    model = Image_color
    extra = 0
    max_num = 8
    min_num = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImgColor]
    readonly_fields = ('quantity', 'new_price')
    list_filter = ('collection',)

    list_display = ['id', 'collection', 'name', 'price', 'discount', 'new_price', 'size_range', 'bestseller', 'new']


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)

from django.contrib import admin
from .models import *



class ProductImgColor(admin.TabularInline):
    model = Image_color
    extra = 0
    max_num = 8
    min_num = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImgColor]


admin.site.register(Product, ProductAdmin)
admin.site.register(Collection)
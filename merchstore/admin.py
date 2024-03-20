from django.contrib import admin

from .models import Product, ProductType


class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType


class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ["name", "price", "type"]
    list_filter = ["type"]
    search_fields = ["name"]


admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)

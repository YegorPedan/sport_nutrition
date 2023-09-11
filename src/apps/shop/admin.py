from django.contrib import admin
from .models import Product, DeliveryPoint, Order, Feedback


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity']
    search_fields = ('name',)


@admin.register(DeliveryPoint)
class DeliveryPointAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    search_fields = ('name',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_products', 'delivery_point', 'status']

    def get_products(self, obj):
        return ', '.join([product.name for product in obj.product.all()])

    get_products.short_description = 'Products'


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['product', 'date', 'product', 'small_desc']
    search_fields = ('product',)

    def small_desc(self, obj):
        return obj.text[:50]

    small_desc.short_description = 'description'
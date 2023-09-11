from django.contrib import admin
from .models import Product, DeliveryPoint, Order, Feedback, ProductImage
from django.utils.html import escape, format_html


class ProductImageInline(admin.TabularInline):  # You can use StackedInline if you prefer a different layout
    model = ProductImage
    extra = 1  # Number of empty image forms to display


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'display_image']
    search_fields = ('name',)
    inlines = [ProductImageInline]

    def display_image(self, obj):
        if obj.images.exists():
            image_url = obj.images.first().url.url  # Assuming you have at least one image per product
            return format_html('<img src="{}" width="50" height="50" />', escape(image_url))
        return format_html('<img src="{}" width="50" height="50" />', escape('path_to_placeholder_image.jpg'))

    display_image.short_description = 'Image'


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

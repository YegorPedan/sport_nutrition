from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=255),
    energy_value = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'product'


class ProductImage(models.Model):
    url = models.ImageField(upload_to='shop_images', null=True, blank=True)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'product_image'


class DeliveryPoint(models.Model):
    address = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'delivery-point'


class Order(models.Model):
    STATUS_CHOICE = [
        ('PR', 'PROCESSING'),
        ('DI', 'DELIVERY'),
        ('DD', 'DELIVERED'),
        ('PA', 'PASSED'),
    ]
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICE,
        default='PR',
    )
    code = models.CharField('The item uniq code', max_length=50),
    product = models.ManyToManyField(Product, related_name='orders')
    delivery_point = models.ForeignKey(to=DeliveryPoint, on_delete=models.CASCADE, related_name='orders')

    class Meta:
        db_table = 'order'


class Feedback(models.Model):
    text = models.TextField()
    mark = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
        ]
    )
    date = models.DateTimeField(auto_now_add=True),
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        db_table = 'feedback'

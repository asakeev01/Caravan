from django.db import models

from apps.categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name = 'products')
    def __str__(self):
        return f'{self.name}'


class Colour(models.Model):
    colour = models.CharField(max_length = 255)

    def __str__(self):
        return self.colour


class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "product_items")
    colour = models.ManyToManyField(Colour)
    price = models.DecimalField(max_digits = 10, decimal_places = 0)

    def __str__(self):
        print(self.colour)
        return f"{self.product.name}'s item of {self.price}"


class Size(models.Model):
    size = models.CharField(max_length = 255)
    hip = models.CharField(max_length = 255)
    waist = models.CharField(max_length = 255)

    def __str__(self):
        return self.size


class Quantity(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete = models.CASCADE, related_name = "quantities")
    size = models.ForeignKey(Size, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('product_item', 'size',)
        verbose_name = 'Quantity'
        verbose_name_plural = 'Quantities'

    def __str__(self):
        return f'The size {self.size} of {self.product_item.product.name} '


class ProductItemImage(models.Model):
    image = models.ImageField(upload_to = 'productImages')
    product_item = models.ForeignKey(ProductItem, on_delete = models.CASCADE, related_name = 'product_item_images')

    def __str__(self):
        return f"{self.product_item.product.name}'s image of item"


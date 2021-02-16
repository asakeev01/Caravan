from rest_framework import serializers

from .models import *
from apps.categories.serializers import *


class SizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Size
        fields = ('size', 'hip', 'waist')


class QuantitySerializer(serializers.ModelSerializer):
    size = SizeSerializer()

    class Meta:
        model = Quantity
        fields = ('product_item', 'size', 'quantity')


class ColourSerializer(serializers.ModelSerializer):

    class Meta:
        model = Colour
        fields = ('colour',)


class ProductItemSerializer(serializers.ModelSerializer):
    colour = ColourSerializer(many = True)
    quantities = QuantitySerializer(many = True)

    class Meta:
        model = ProductItem
        fields = ('product', 'colour', 'price', 'quantities')


class ProductSerializer(serializers.ModelSerializer):
    product_items = ProductItemSerializer(many = True)
    categories = CategorySerializer(many = True)

    class Meta:
        model = Product
        fields = ('name', 'description', 'categories', 'product_items')






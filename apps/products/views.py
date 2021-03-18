from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .models import *
from .serializers import *

from rest_framework import generics


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImageView(generics.RetrieveAPIView):
    queryset = ProductItemImage.objects.all()
    serializer_class = ProductItemImageSerializer

    

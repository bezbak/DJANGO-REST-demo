# from django.shortcuts import render
from rest_framework import generics

from .serializers import ProductSerializer, ProductShotsSerializer

from .models import Product, ProductShots


class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductShotsAPIView(generics.ListAPIView):
    queryset = ProductShots.objects.all()
    serializer_class = ProductShotsSerializer
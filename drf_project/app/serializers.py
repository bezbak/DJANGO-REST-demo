from rest_framework import serializers

from .models import Product, ProductShots

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'cat', 'draft', 'description', 'price','oc', 'pros','ram', 'vidyha', 'storage', 'region', 'activate')
class ProductShotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductShots
        fields = ('title', 'image', 'description','Product')
        
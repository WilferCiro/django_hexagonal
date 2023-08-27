from rest_framework import serializers

from app.products.infrastructure.models.models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['title', 'price']

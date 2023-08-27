from rest_framework import serializers

class ProductCreateDtoSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)

class ProductUpdateDtoSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)
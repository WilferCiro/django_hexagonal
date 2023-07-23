from django.contrib.auth.models import User, Group
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'groups']

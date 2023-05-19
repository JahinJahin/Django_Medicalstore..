from catalog.models import medicine
from rest_framework import serializers
from django.contrib.auth.models import User


class medicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicine
        fields='__all__'


class signupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

    def create(self,validated_data):
        user=User.objects.create_superuser(**validated_data)
        return user
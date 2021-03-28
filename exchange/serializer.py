from rest_framework import serializers
from .models import Exchange

class ExchangeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exchange
        fields = ['id', 'created_at','margin','Exchange_rate']

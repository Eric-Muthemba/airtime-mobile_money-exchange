from rest_framework import serializers
from .models import Transactions


class ExpensesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transactions
        ordering=("-created_at",)
        fields = ['id', 'from_phoneNumber','created_at','updated_at', 'credit_amount', 'cash_amount','category']
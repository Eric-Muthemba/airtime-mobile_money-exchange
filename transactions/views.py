from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveAPIView ,RetrieveUpdateDestroyAPIView
from .serializer import ExpensesSerializer
from .models import Transactions


class ExpenseListAPIView(ListCreateAPIView):
    serializer_class = ExpensesSerializer
    queryset = Transactions.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return self.queryset.filter()


class ExpenseDetailAPIView(RetrieveAPIView):
    serializer_class = ExpensesSerializer
    queryset = Transactions.objects.all()
    lookup_field = "from_phoneNumber"

    def get_queryset(self):
        from_phoneNumber = self.kwargs['from_phoneNumber']
        queryset = self.queryset.filter(from_phoneNumber=from_phoneNumber)
        print(queryset)
        id = self.kwargs['id']-1
        id = queryset[id].id
        return queryset.filter(id=id)

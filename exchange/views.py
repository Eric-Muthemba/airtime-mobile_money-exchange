from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import views,status
from rest_framework.response import Response
from .serializer import ExchangeSerializer
from .models import Exchange


class ExchangeListAPIView(ListCreateAPIView):
    serializer_class = ExchangeSerializer
    queryset = Exchange.objects.all()

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        print(self.queryset.filter()[0].created_at)
        return self.queryset.filter()

class CurrentExchangeAPIView(views.APIView):
    serializer_class = ExchangeSerializer

    def get(self,request):
        current_E_R = Exchange.objects.last().Exchange_rate

        return Response({"Exchange_rate":current_E_R})

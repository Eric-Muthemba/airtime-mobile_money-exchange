from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExchangeListAPIView.as_view(), name="rates"),
    path('latest/', views.CurrentExchangeAPIView.as_view(), name='rates'),

]
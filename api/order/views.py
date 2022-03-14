# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .serializers import OrderSerializer
from .models import Order   

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('order_name')
    serializer_class = OrderSerializer

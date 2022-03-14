from .models import Order
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(OrderSerializer, self).__init__(*args, **kwargs)
        
    class Meta:
        model = Order
        fields = ("order_name","stock")
        fields = '__all__'

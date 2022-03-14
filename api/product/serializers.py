from .models import Product
from rest_framework import serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(ProductSerializer, self).__init__(*args, **kwargs)
    
    class Meta:
        model = Product
        fields = {
            "name", "amount_in_stock"
        }
        fields = '__all__'
    
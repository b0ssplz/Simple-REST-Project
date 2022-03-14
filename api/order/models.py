from api.product.models import Product
from django.db import models

class Order(models.Model):
    order_name = models.CharField(max_length=50)
    stock = models.CharField(max_length=50)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.order_name
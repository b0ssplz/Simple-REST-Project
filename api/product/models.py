from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    amount_in_stock = models.IntegerField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.name
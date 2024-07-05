from django.db import models
from main.models import Product
# Create your models here.

class CartProducts(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    price = models.IntegerField(default=0)



class Cart(models.Model):
    sessionkey = models.CharField(max_length=200,editable=False)
    products = models.ManyToManyField(CartProducts)
    total_quantity = models.IntegerField(default=0)
    total_price = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.product.title
    
    
    
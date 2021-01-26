from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    emailid = models.EmailField()
    ipaddr = models.GenericIPAddressField()
    
    def __str__(self): 
        return self.name

class Product(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,
                            on_delete=models.CASCADE,
                            related_name="products")
    name = models.CharField(max_length=255)
    productcode = models.IntegerField()
    photo = models.ImageField(blank=True,null=True)
    productdescription = models.TextField(blank=True, null=True)
    price = models.FloatField()
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name

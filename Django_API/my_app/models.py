from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100,null=True)
    code = models.CharField(max_length=100,null=True)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.product_name
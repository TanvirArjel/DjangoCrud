from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    quantity = models.IntegerField()
    product_image = models.ImageField(max_length = 200,null=True)

    def __str__(self):
        return self.product_name

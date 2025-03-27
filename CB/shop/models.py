from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Mark it as primary!
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    Product_des=models.CharField(max_length=300)
    pub_date = models.DateField()  # Fixed typo from 'pub_dat'




from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)  # Mark it as primary!
    product_name = models.CharField(max_length=100)
    category=models.CharField(max_length=100,default="")
    subcategory = models.CharField(max_length=100,default="")
    product_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    product_des=models.CharField(max_length=300)
    pub_date = models.DateField()  # Fixed typo from 'pub_dat'
    image=models.ImageField(upload_to="shop/images",default="")
    def __str__(self):
        return self.product_name





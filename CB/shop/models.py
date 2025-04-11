from django.db import models
from datetime import datetime
# from django.db import models
# from .models import Order

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

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name


class Orders(models.Model):
    items_json = models.TextField()
    name = models.CharField(max_length=90)
    email = models.EmailField()
    address1 = models.CharField(max_length=111)
    address2 = models.CharField(max_length=111)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    order_date = models.DateTimeField(auto_now_add=True)
    # order_date = models.DateTimeField(auto_now_add=True)
    # timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.name}"
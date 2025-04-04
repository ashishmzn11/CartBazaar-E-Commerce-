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

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name
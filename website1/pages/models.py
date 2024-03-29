from django.db import models

# Create your models here.
class Contact(models.Model):
    con_name = models.CharField(max_length = 255)
    con_email = models.EmailField(max_length = 255)
    con_msg = models.TextField()


    def __str__(self):
        return self.con_name
    
class Register(models.Model):
    reg_name = models.CharField(max_length = 255)
    reg_email = models.EmailField(max_length = 255)
    reg_phone = models.CharField(max_length = 255)
    reg_username = models.CharField(max_length = 255)
    reg_password = models.CharField(max_length = 255)


    def __str__(self):
        return self.reg_name
    
class Product(models.Model):
    pro_name = models.CharField(max_length = 255)
    pro_price = models.FloatField(max_length = 255)
    pro_image = models.FileField(null=True,upload_to="products")
    


    def __str__(self):
        return self.pro_name
    
class Cart(models.Model):
    cart_user = models.CharField(max_length=250,default=None)  
    cart_proid = models.IntegerField(null=True)
    cart_name = models.CharField(max_length=250) 
    cart_price = models.FloatField(max_length=250)
    cart_image = models.FileField(null=True)
    cart_qty = models.IntegerField()
    cart_amount = models.FloatField()


    def __str__(self):
        return self.cart_name
    
class Order(models.Model):
    ord_user = models.CharField(max_length=250,default=None)  
    ord_name = models.CharField(max_length=250) 
    ord_price = models.FloatField(max_length=250)
    ord_image = models.FileField(null=True)
    ord_qty = models.IntegerField()
    ord_amount = models.FloatField()
    ord_address = models.TextField(null=True)
    ord_dlvtype = models.CharField(null=True,max_length=10)
    ord_status = models.IntegerField(null=True)


    def __str__(self):
        return self.ord_name
    

    

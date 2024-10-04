from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

    

class SellerData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=70,null=True)
    number=models.CharField(max_length=70,null=True)
    img=models.ImageField(upload_to='image/',null=True)
    state=models.CharField(max_length=70,null=True)
    country=models.CharField(max_length=70)
    Join_Date=models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    

class CategoryModel(models.Model):
    Category_Name=models.CharField(max_length=70)

class SubCategoryModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    SubCategory_Name=models.CharField(max_length=70)

class ProductModel(models.Model):
    Category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE,null=True)
    SubCategory=models.ForeignKey(SubCategoryModel,on_delete=models.CASCADE,null=True)
    Product_Name=models.CharField(max_length=70) 
    Product_Discription=models.CharField(max_length=70)   
    Product_Price=models.IntegerField() 
    
    Join_Date=models.DateField(auto_now_add=True)
    seller=models.ForeignKey(SellerData,on_delete=models.CASCADE,null=True)
    approved = models.BooleanField(default=False)
    stock = models.BooleanField(default=True)
  



class ProductImage(models.Model):
    Product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True) 
    image = models.ImageField(upload_to='product_images/') 
    

class CartModel(models.Model):
    Customer=models.ForeignKey(SellerData,on_delete=models.CASCADE,null=True)
    Product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    Image=models.ForeignKey(ProductImage,on_delete=models.CASCADE,null=True)     

class BillingData(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    companyname=models.CharField(max_length=70)
    housenumber=models.CharField(max_length=70)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    image=models.ForeignKey(ProductImage,on_delete=models.CASCADE,null=True)
    pincode=models.IntegerField() 
    landmark=models.CharField(max_length=70)
    order_Date=models.DateField(auto_now_add=True)
    
    seller=models.ForeignKey(SellerData,on_delete=models.CASCADE,null=True)
 
   

class PaymentData(models.Model):
    cardnumber=models.IntegerField() 
    cardname=models.CharField(max_length=70)
    day=models.IntegerField() 
    year=models.IntegerField() 
    securitycode=models.IntegerField() 
    order_Date=models.DateField(auto_now_add=True)
    
    
  
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    image=models.ForeignKey(ProductImage,on_delete=models.CASCADE,null=True)
    seller=models.ForeignKey(SellerData,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
 


class ReviewData(models.Model):
    review=models.CharField(max_length=70)
    star=models.IntegerField() 
    payment=models.ForeignKey(PaymentData,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
  
    seller=models.ForeignKey(SellerData,on_delete=models.CASCADE,null=True)
    image=models.ForeignKey(ProductImage,on_delete=models.CASCADE,null=True)


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

 
    seller=models.ForeignKey(SellerData,on_delete=models.CASCADE,null=True)

 


 
class UserLocation(models.Model):
    Prod=models.ForeignKey(ProductModel,on_delete=models.CASCADE,null=True)
    latitude = models.FloatField()
    longitude = models.FloatField()
   



from django.db import models
from tinymce.models import HTMLField
from grocery.models import *
import datetime
from django.contrib.auth.models import User



Gender=(
    ('Male','Male'),
    ('Female','Female'),
)


class Category(models.Model):
    Category_Name=models.CharField(max_length=100)
    Pic=models.ImageField(upload_to='category/', default="")
    Register_Date=models.DateField(default=datetime.date.today())
    Status=models.CharField(max_length=50,default='inactive')
    class Meta:
        db_table="Category"
    def __str__(self):
        return self.Category_Name    
    
class Product(models.Model):
    Photo=models.ImageField(upload_to='product1/')
    Product_Name=models.CharField(max_length=100)
    Categoryid=models.ForeignKey(Category, on_delete=models.CASCADE)
    MRP=models.FloatField(default=0.0)
    Selling_Price=models.FloatField()
    Opening_Stock=models.FloatField()
    Register_Date=models.DateField(default=datetime.date.today())
    Status=models.CharField(max_length=100)
    Description=HTMLField()
    class Meta:
        db_table="Product"
    def __str__(self):
        return self.Product_Name    
    

class Supplier(models.Model):
    Categoryid=models.ForeignKey(Category, on_delete=models.CASCADE, default="")
    Supplier_Pic=models.ImageField(upload_to='supplier/', default="")
    Supplier_Name=models.CharField(max_length=50)
    Register_Date=models.DateField(default=datetime.date.today())
    Email=models.CharField(max_length=100)
    Phone_No=models.CharField(max_length=20)
    City=models.CharField(max_length=50,default="")
    class Meta:
        db_table="Supplier"
    def __str__(self):
        return self.Supplier_Name

class Purchase(models.Model):
    Productid=models.ForeignKey(Product, on_delete=models.CASCADE)
    Employeprofileid=models.ForeignKey(User,on_delete=models.CASCADE,default="")
    Supplierid=models.ForeignKey(Supplier, on_delete=models.CASCADE)
    Date=models.DateField(default=datetime.date.today())
    Quantity=models.IntegerField()
    MRP=models.FloatField(default=0,blank=True,null=True)
    Total=models.IntegerField(default=0, blank=True,null=True)
    Paid=models.FloatField()
    Payment_Status=models.CharField(max_length=50,default="")
    Purchase_Status=models.CharField(max_length=50,default="")
    class Meta:
        db_table="Purchase"
    def __str__(self):
        return self.Payment_Status    
    
class Employeprofile(models.Model):
    Employe_Id=models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    Picture=models.ImageField(upload_to='employeprofile/', default="")
    Employe_Name=models.CharField(max_length=50)
    Username=models.CharField(max_length=100)
    Gender=models.CharField(max_length=50, choices=Gender) 
    Date_Of_Join=models.DateField(default=datetime.date.today()) 
    Contact_No=models.CharField(max_length=12)
    Email=models.CharField(max_length=100)
    Address=models.TextField()
    class Meta:
        db_table="Employeprofile"
    def __str__(self):
        return self.Employe_Name

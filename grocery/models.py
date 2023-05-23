from django.db import models
from dashboard.models import *
from dashboard.models import Product
from django.contrib.auth.models import User

# Create your models here.
class contact1(models.Model):
    name=models.CharField(max_length=100)
    phone=models.IntegerField()
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    message=models.TextField()
    class Meta:
        db_table="contact1"


class newsletter(models.Model):
    email=models.CharField(max_length=50)
    class Meta:
        db_table="newsletter"    

class faq(models.Model):
    Question=models.TextField()
    Answer=models.TextField()
    class Meta:
        db_table="faq"


class review(models.Model):
    Userid=models.ForeignKey(User,on_delete=models.CASCADE)
    Productid=models.ForeignKey(Product, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=500)
    rating=models.CharField(max_length=50)
    class Meta:
        db_table="review"


class like(models.Model):
    Userid=models.ForeignKey(User,on_delete=models.CASCADE)
    Productid=models.ForeignKey(Product, on_delete=models.CASCADE)
    class Meta:
        db_table="like"


class fav(models.Model):
    Userid=models.ForeignKey(User,on_delete=models.CASCADE)
    Productid=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='products')
    class Meta:
        db_table="fav"
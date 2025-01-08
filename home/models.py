from django.db import models
class REGISTER(models.Model):
    
    Hotel=models.CharField(max_length=122)
    city=models.CharField(max_length=122)
    checkindate=models.TextField()
    checkoutdate=models.TextField()
    budget=models.IntegerField()
    num=models.IntegerField()
    username=models.CharField(max_length=122,default="No username")
    messsage=models.CharField(max_length=122,default="No message")
    phone=models.CharField(max_length=12,default="No Phone number mentioned")
    country=models.CharField(max_length=122 ,default="No country" )
    def __str__(self):
      return self.checkindate
class Contactus(models.Model):
   name=models.CharField(max_length=122)
   messagess=models.CharField(max_length=222)
   phone=models.IntegerField()
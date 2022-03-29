from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(unique= True)
    username=models.CharField(max_length = 20,unique= True,default="default_123")
    password = models.CharField(max_length = 20)
    otp = models.IntegerField(default = 459)
    is_active = models.BooleanField(default=True)
    is_verfied = models.BooleanField(default=False)
    created_at= models.DateTimeField(auto_now_add=True,blank=False)
    updated_at = models.DateTimeField(auto_now = True, blank=False)

class customer(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    fullname=models.CharField(max_length=50,default="default")
    phone=models.CharField(max_length=10,default="default")
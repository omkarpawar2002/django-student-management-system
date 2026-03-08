from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField(default="1900-01-01")
    gender = models.CharField(max_length=10)
    mobile_no = models.CharField(max_length=15)
    fav_language = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=100)
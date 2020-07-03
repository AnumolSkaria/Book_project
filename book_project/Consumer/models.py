from django.db import models

# Create your models here.

class Consumer(models.Model):
    c_name=models.CharField(max_length=250)
    email=models.EmailField(max_length=150)
    phone=models.CharField(max_length=12)
    username=models.CharField(max_length=150,unique=True)
    password=models.CharField(max_length=150)

    def __str__(self):
        return self.username





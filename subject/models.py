from pyexpat import model
from django.db import models

# Create your models here.

class benefit(models.Model):
    id= models.IntegerField(primary_key=True)
    title= models.CharField(max_length=200)

class topic(models.Model):
    title= models.CharField(max_length=200)

class pin_point(models.Model):
    title= models.CharField(max_length=200)
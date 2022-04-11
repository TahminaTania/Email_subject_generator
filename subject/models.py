from django.db import models

# Create your models here.

class benefit(models.Model):
    title= models.CharField(max_length=200)

class topic(models.Model):
    title= models.CharField(max_length=200)

class pin_point(models.Model):
    title= models.CharField(max_length=200)
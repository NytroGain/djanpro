from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)

class Category(models.Model):
    title = models.CharField(max_length=255)
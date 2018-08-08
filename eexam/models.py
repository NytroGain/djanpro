from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return self.first_name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class UserEmail(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email

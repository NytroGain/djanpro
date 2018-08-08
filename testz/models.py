from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class UserEmail(models.Model):
    first_name = models.CharField(max_length=30,null=True, blank=True)
    last_name = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.email

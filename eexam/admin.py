from django.contrib import admin
from .models import Customer ,Blog ,UserEmail
# Register your models here.
admin.site.register(Customer)
admin.site.register(Blog)
admin.site.register(UserEmail)
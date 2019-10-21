from django.contrib import admin
from .models import Product_field,User_field,Buyed_product
# Register your models here.
admin.site.register(Product_field)
admin.site.register(User_field)
admin.site.register(Buyed_product)

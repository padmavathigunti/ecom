from django.db import models

# Create your models here.
class Product_field(models.Model):
    Product_name = models.CharField(max_length = 25)
    Product_description = models.CharField(max_length = 25)
    Product_cost = models.IntegerField()
    no_of_products = models.CharField(max_length = 25)

    def __str__(self):
        return self.Product_name


class User_field(models.Model):
    Username = models.CharField(max_length = 25)
    email = models.CharField(max_length = 25)
    phone_number = models.CharField(max_length = 10)
    Account_balance = models.IntegerField()

    def __str__(self):
        return self.Username


class Buyed_product(models.Model):
    Product_name = models.CharField(max_length = 25)
    user_email = models.CharField(max_length = 25)
    cost_product = models.CharField(max_length = 25)

    def __str__(self):
        return self.Product_name


class buyed(models.Model):
    user = models.ForeignKey(User_field,on_delete=models.CASCADE)
    product = models.ForeignKey(Product_field,on_delete=models.CASCADE)

    def __str__(self):
        return "{}---{}".format(self.product,self.user)   

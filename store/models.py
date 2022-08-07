from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE) # user can only have one customer and customer can only have one user/ delete it if the user item is deleted
    name = models.CharField(max_length=200, null = True)
    email = models.CharField(max_length=200, null = True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null = True)
    price = models.FloatField(null = True)
    digital = models.BooleanField(default= False, null = True, blank=True) #if the item is digital that no shipping needed
    #image

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)# customer 1:n relationship. If the Customer is delete, we dont want to delete the order
    #Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user.
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default=False)
    #if the cart is complete. If yes, cannot add more items
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)



class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null = True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null = True)
    address = models.CharField(max_length=200, null = True)
    city = models.CharField(max_length=200, null = True)
    state = models.CharField(max_length=200, null = True)
    zipcode = models.CharField(max_length=200, null = True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

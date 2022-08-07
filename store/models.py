from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# The @property is a built-in decorator for the property() function in Python. It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.

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
    image = models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.name

  # if no image uplaod, no image url
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url






class Order(models.Model):# summary of the cart
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True,blank=True)# customer 1:n relationship. If the Customer is delete, we dont want to delete the order
    #Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user.
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete =models.BooleanField(default=False)
    #if the cart is complete. If yes, cannot add more items
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):# get the total item number in the cart/order
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems]) #call function under Orderitem
        return total # retrurn total price

    @property
    def get_cart_items(self):  # get the total item number in the cart/order
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total




class OrderItem(models.Model):# for each item in the cart
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null = True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL, null = True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


    @property
    def get_total(self):#get total price for each item in the order
        total = self.product.price * self.quantity
        return total

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

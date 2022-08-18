import json

from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
from .utiles import cookieCart
# Create your views here.

def store_view(request, *args, **kwargs):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # try:get expect: create&save
        items = order.orderitem_set.all()  # get all the order items with order as a parent
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']
    print(cartItems)
    products = Product.objects.all()
    context = {'products': products,'cartItems': cartItems}


    return render(request,'store/store.html',context)


def cart_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer,complete=False)# try:get expect: create&save
        items = order.orderitem_set.all()# get all the order items with order as a parent
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order =cookieData['order']
        items = cookieData['items']

    products = Product.objects.all()
    context = {'items':items,'order':order, 'cartItems': cartItems}
    return render(request,'store/cart.html',context)


def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # try:get expect: create&save
        items = order.orderitem_set.all()  # get all the order items with order as a parent
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping':False}
        cartItems = order['get_cart_items']

    # order.check_items_name



    context = {'items':items,'order':order,'cartItems': cartItems}
    return render(request,'store/checkout.html',context)


def updateitem_view(request):
    data = json.loads(request.body)
    print(data)
    # body:JSON.stringify({'productID': productId,'Action:':action})
    productId = data['productId']
    action = data['action']
    print('Action:',action)
    print('Prodcut',productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)  # try:get expect: create&save

#create a cart there
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)

#check items in the cart
    if action =='add':
        orderItem.quantity = (orderItem.quantity +1 )
    elif action =='remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()

    if orderItem.quantity <= 0 :
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
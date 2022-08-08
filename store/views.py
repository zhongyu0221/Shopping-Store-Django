from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.

def store_view(request, *args, **kwargs):
    products = Product.objects.all()
    context = {'products': products}

    checkuser=request.user
    print('checkuser:',checkuser)
    return render(request,'store/store.html',context)


def cart_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order,created = Order.objects.get_or_create(customer = customer,complete=False)# try:get expect: create&save
        items = order.orderitem_set.all()# get all the order items with order as a parent
    else:
        items = []
        order = {'get_cart_total':0,'get_cart_items':0}

    context = {'items':items,'order':order}
    return render(request,'store/cart.html',context)


def checkout_view(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)  # try:get expect: create&save
        items = order.orderitem_set.all()  # get all the order items with order as a parent
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}



    context = {'items':items,'order':order}
    return render(request,'store/checkout.html',context)


def updateitem_view(request):
    return JsonResponse('Item was added', safe=False)
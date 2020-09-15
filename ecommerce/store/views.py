from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.
def store(requests):
	products = Product.objects.all()
	return render(requests, 'store/store.html', {'products': products})

def checkout(requests):
	if requests.user.is_authenticated:
			customer = requests.user.customer
			order, created = Order.objects.get_or_create(customer=customer, complete=False)
			items = order.orderitem_set.all()
	else:
			items = []
			order = {'get_cart_total':0, 'get_cart_items':0}
		
	context = {'items' : items, 'order': order}
	return render(requests,'store/checkout.html', context)

def cart(requests):
	if requests.user.is_authenticated:
		customer = requests.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items' : items, 'order': order}
	return render(requests,'store/cart.html', context)
def updateItem(requests):
	return JsonResponse('Item was Added', safe = False)
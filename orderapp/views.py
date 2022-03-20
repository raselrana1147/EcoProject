from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from orderapp.models import Cart
from product.models import Category
from django.utils.crypto import get_random_string
from orderapp.models import Order, OrderProduct
from userapp.models import UserProfile

# Create your views here.
def order(request):
	return HttpResponse("this order page")

def add_to_cart(request,id):
	url=request.META.get('HTTP_REFERER')
	current_user=request.user
	if request.method=="POST":
		product_id=int(id)
		quantity=request.POST.get('quantity')
		cart=Cart.objects.filter(product_id=product_id,user_id=current_user.id)
		if cart:
			cart[0].quantity +=int(quantity)
			cart[0].save() 
		else:
			data=Cart()
			data.product_id=product_id
			data.user_id=current_user.id
			data.quantity=quantity
			data.save()

	else:
		cart=Cart.objects.filter(product_id=id,user_id=current_user.id)
		if cart:
			cart[0].quantity +=1
			cart[0].save() 
		else:
			data=Cart()
			data.product_id=id
			data.user_id=current_user.id
			data.quantity=1
			data.save()
	messages.success(request, 'Product has been added into cart.')
	return HttpResponseRedirect(url)

def view_cart(request):

	current_user=request.user
	carts=Cart.objects.filter(user_id=current_user.id)
	total_amount=0
	if carts:
		for cart in carts:
			total_amount +=cart.quantity*cart.product.new_price
	context={
		'carts':carts,
		'total_amount':total_amount
	}
	return render(request,'view_cart.html',context)


def cart_destroy(request,id):
	url=request.META.get('HTTP_REFERER')
	cart=Cart.objects.filter(id=id)
	cart.delete()
	messages.success(request, 'Item has been removed from the cart.')
	return HttpResponseRedirect(url)

@login_required(login_url='/user/login_register')
def checkout(request):
	if request.method=="POST":
		first_name=request.POST.get('first_name')
		last_name=request.POST.get('last_name')
		phone=request.POST.get('phone')
		country=request.POST.get('country')
		city=request.POST.get('city')
		address=request.POST.get('address')
		adminnote=request.POST.get('adminnote')
		transaction_id=request.POST.get('transaction_id')
		sub_total=request.POST.get('sub_total')

		order=Order()

		order.first_name=first_name
		order.last_name=last_name
		order.phone=phone
		order.country=country
		order.city=city
		order.address=address
		order.adminnote=adminnote
		order.transaction_id=transaction_id
		order.code=get_random_string(5).upper()
		order.total=sub_total
		order.ip=request.META.get('REMOTE_ADDR')
		order.user_id=request.user.id
		order.save()

		carts=Cart.objects.filter(user_id=request.user.id)
		for cart in carts:
			order_product=OrderProduct()

			order_product.user_id=request.user.id
			order_product.order_id=order.id
			order_product.product_id=cart.product_id
			order_product.quantity=cart.quantity
			order_product.price=cart.product.new_price
			order_product.amount=cart.product.new_price*cart.quantity
			order_product.save()

		Cart.objects.filter(user_id=request.user.id).delete()
		context={
		'ordercode':order.code,
		'total_amount':order.total
	    }
		return render(request,'order_complete.html',context)
	else:
		carts=Cart.objects.filter(user_id=request.user.id)
		profile=UserProfile.objects.get(user_id=request.user.id);

		sub_total=0
		if carts:
			for cart in carts:
				sub_total +=cart.product.new_price*cart.quantity
		else:
			sub_total=0
			
		context={
		'carts':carts,
		'sub_total':sub_total,
		'profile':profile
	    }
	return render(request,'checkout.html',context)


@login_required(login_url='/user/login_register')
def order_list(request):
	
	orders=Order.objects.filter(user_id=request.user.id)
	context={
		'orders':orders
	    }
	return render(request,'order_list.html',context)



@login_required(login_url='/user/login_register')
def order_product_list(request,id):
	products=OrderProduct.objects.filter(order_id=id)
	context={
		'products':products
	    }
	return render(request,'order_product_list.html',context)



@login_required(login_url='/user/login_register')
def billing_detail(request,id):
	billing=Order.objects.get(id=id)
	products=OrderProduct.objects.filter(order_id=id)
	context={
		'billing':billing,
		'products':products
	}

	return render(request,'billing_detail.html',context)



		


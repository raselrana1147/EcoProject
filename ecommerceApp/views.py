from django.shortcuts import (
		render,
		HttpResponse,
		redirect,
		HttpResponseRedirect
	)
from ecomapp.models import Setting,Slider
from product.models import (
	Product,
	Images,
	Category,
	Comment,
	Color,
	Size,
	Varient
)
from ecommerceApp.models import ContactUs,Faq
from orderapp.models import Cart
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
	sliders=Slider.objects.all().order_by('id')
	products=Product.objects.all().order_by('-id')
	featureds=Product.objects.all().order_by('id')
	carts=Cart.objects.filter(user_id=request.user.id)
	total_amount=0;
	if carts:
		for cart in carts:
			total_amount+=cart.quantity*cart.product.new_price
		
	context={
		'sliders':sliders,
		'products':products,
		'featureds':featureds,
		'total_amount':total_amount,
		'carts':carts
	}
	return render(request,'index.html',context)

def product_detail(request,slug):
	product=Product.objects.get(slug=slug)
	product_id=product.id
	images=Images.objects.filter(product=product_id)
	related_products=Product.objects.order_by("?")[:10]
	comments=Comment.objects.filter(product_id=product_id,status='True')

	context={
		'product':product,
		'images':images,
		'related_products':related_products,
		'comments':comments
	}

	if product.variant !="None":
		if request.method=="POST":

			variant_id=request.POST.get('variant_id')
			variant=Varient.objects.get(id=variant_id)
			colors=Varient.objects.filter(product_id=id,size_id=variant.size_id)
			sizes=Varient.objects.raw('SELECT * FROM product_varient WHERE product_id=%s GROUP BY size_id',[id])
			query=variant.title+' Size' + str(variant.size) + ' Color'+ str(variant.color)
		else:
			variants=Varient.objects.filter(product_id=product.id)
			if variants =="":
				colors=Varient.objects.filter(product_id=product.id, size_id=variants[0].size_id)
				sizes=Varient.objects.raw('SELECT * FROM product_varient WHERE product_id=%s GROUP BY size_id',[id])
				variant=Varient.objects.get(id=variants[0].id)
				context.update({
						'colors':colors,
						'sizes':sizes,
						'variant':variant
					})

	return render(request,'single_product.html',context)

def ajaxColor(request):
	data={}
	if request.POST.get('action') == "POST":
		size_id=request.POST.get('size')
		product_id=request.POST.get('product_id')
		colors=Varient.objects.filter(product_id=product_id,size_id=size_id)
		context={
			'size_id':size_id,
			'product_id':product_id,
			'colors':colors
		}
		data={'rendered_table':render_to_string('color_list.html',context=context)}
		return JsonResponse(data)
	return JsonResponse(data)

def category_wise_product(request,categoty_id):
	products=Product.objects.filter(category=categoty_id).order_by('-id')
	

	context={
		'products':products,
	}
	return render(request,'category_product.html',context)

def subcategory_wise_product(request,subcategoty_id):
	products=Product.objects.filter(category=subcategoty_id).order_by('-id')
	
	context={
		'products':products,
	}
	return render(request,'subcategory_product.html',context)

def about_us(request):
	
	return render(request,'about_us.html')

def contact_us(request):
	
	if request.method=="POST":
		
		contact        =ContactUs()
		name           =request.POST.get('name')
		email          =request.POST.get('email')
		subject        =request.POST.get('subject')
		message        =request.POST.get('message')
		contact.name   =name
		contact.email  =email
		contact.subject=subject
		contact.message=message

		contact.save()
		return render(request,'contact_us.html')
	else:
		return render(request,'contact_us.html')

def search_item(request):
	
	if request.method=="POST":
		search_key=request.POST.get('search_key')
		category_id=request.POST.get('category_id')
		if category_id==0:
			products=Product.objects.filter(title__icontains=search_key)
		else:
			products=Product.objects.filter(title__icontains=search_key,category_id=category_id)
		context={
			
			'products':products
		}
		return render(request,'search_product.html',context)
	   

	return redirect("ecommerce:home_page")

@login_required(login_url='/user/login_register')
def send_review(request):
	url=request.META.get('HTTP_REFERER')
	if request.method=="POST":
		review=Comment()
		review.subject=request.POST.get('subject')
		review.comment=request.POST.get('comment')
		review.rating=request.POST.get('rating')
		review.user_id=request.user.id
		review.product_id=request.POST.get('product_id')
		review.save()
		messages.success(request, 'Review submited successfully.')
		return HttpResponseRedirect(url)
	else:
		return HttpResponseRedirect(url)

def faqs(request):
	url=request.META.get('HTTP_REFERER')
	if request.method=="POST":
		faq=Faq()
		faq.question=request.POST.get('question')
		faq.save()
		messages.success(request, 'Your question has been submitted.')
		return HttpResponseRedirect(url)
	else:
		faqs=Faq.objects.filter(status='True').order_by('-id')
		context={
				'faqs':faqs
			}
	return render(request,'faq.html',context)

		


		



		
	

from django.db import models
from django.contrib.auth.models import User
from product.models import Product
from django.utils.safestring import mark_safe

# Create your models here.

class Cart(models.Model):
	product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	quantity=models.IntegerField(default=1)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product.title

	def product_price(self):
		return self.product.new_price

	def unit_total(self):
		return self.product.new_price*self.quantity

			



status=(
		('New','New'),
		('Accepted','Accepted'),
		('Processing','Processing'),
		('Onshipping','Onshipping'),
		('Completed','Completed'),
		('Canceled','Canceled')
	)

class Order(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	first_name=models.CharField(max_length=191)
	last_name=models.CharField(max_length=191)
	code=models.CharField(max_length=191,editable=False)
	phone=models.CharField(max_length=191,blank=True)
	address=models.TextField(max_length=1000,blank=True)
	city=models.CharField(max_length=191,blank=True)
	country=models.CharField(max_length=191,blank=True)
	total=models.FloatField()
	status=models.CharField(max_length=191,choices=status,default='New')
	transaction_id=models.CharField(max_length=191,blank=True)
	ip=models.CharField(max_length=191,blank=True)
	transaction_image=models.ImageField(upload_to='transaction_image/', blank=True)
	adminnote=models.CharField(max_length=191,blank=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.first_name

	def image_tag(self):
		return mark_safe('<img src="{}" alt="transaction image" style="width:100px;height:80px" />'.format(self.transaction_image))

class OrderProduct(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	order=models.ForeignKey(Order,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity=models.IntegerField()
	price=models.FloatField()
	amount=models.FloatField()
	status=models.CharField(max_length=191,choices=status,default='New')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.product.title

	def amountnow(self):
		return self.price*self.quantity
	    





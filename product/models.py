from django.db import models
from django.template.defaultfilters import slugify
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
from django.db.models import Count,Sum,Avg

# Create your models here.


class Category(models.Model):

	STATUS=(
			('True','True'),
			('False','False'),
		)

	parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')
	title=models.CharField(max_length=191)
	keyword=models.CharField(max_length=191)
	image=models.ImageField(upload_to='category/', blank=True)
	slug=models.SlugField(null=True,unique=True)
	status=models.CharField(max_length=191,choices=STATUS)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def subCat(self):
		if self.parent:
			return self.parent.title

	

	class MPTTMeta:
		order_insertion_by = ['title']

	def __str__(self):
		return self.title

	def image_tag(self):
		img=mark_safe('<img src="{}" width="100" height="80" alt="product image" />'.format(self.image.url))
		return img


class Product(models.Model):
	status=(
			('True','True'),
			('False','False'),
		)

	variant=(
			('None','None'),
			('Size','Size'),
			('Coloe','Coloe'),
			('SizeColor','SizeColor'),

		)

	category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='category')
	title=models.CharField(max_length=191)
	keyword=models.CharField(max_length=191)
	image=models.ImageField(upload_to='product')
	new_price=models.DecimalField(decimal_places=2, max_digits=15,default=0)
	old_price=models.DecimalField(decimal_places=2, max_digits=15,default=0)
	amount=models.IntegerField(default=0)
	min_amount=models.IntegerField(default=0)
	description=models.TextField()
	status=models.CharField(max_length=191,choices=status)
	variant=models.CharField(max_length=191, choices=variant, default='New')
	slug=models.SlugField(null=True,unique=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def image_tag(self):
		img=mark_safe('<img src="{}" width="100" height="80" alt="product image" />'.format(self.image.url))
		return img

	def stock(self):
		if self.status=="True":
			return mark_safe('<button class="btn btn-success btn-sm">In Stock</button>')
		else:
			return mark_safe('<button class="btn btn-danger btn-sm">Stock Out</button>')
	def get_absulate_url(self):
		return reverse('priduct_element', kwargs={'slug':self.slug})

	def avarage_review(self):

		reviews=Comment.objects.filter(product_id=self,status=True).aggregate(avarage=Avg('rating'))
		avg=0

		if reviews['avarage'] is not None:
			avg=float(reviews['avarage'])
			return avg
		else:
			return avg


	def total_review(self):

		reviews=Comment.objects.filter(product_id=self,status=True).aggregate(count=Count('id'))
		cnt=0
		
		if reviews['count'] is not None:
			cnt=float(reviews['count'])
			return cnt
		  

class Images(models.Model):
	product=models.ForeignKey(Product, on_delete=models.CASCADE,related_name='product')
	title=models.CharField(max_length=191, blank=True)
	image=models.ImageField(upload_to='gallery')


	def __str__(self):
		return self.title
		
	def show_image(self):
		return mark_safe('<img src="{}" width="100" height="80" alt="gallery image" />'.format(self.image.url))

class Comment(models.Model):
	status=(
			('New','New'),
			('True','True'),
			('False','False')
		)

	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	subject=models.CharField(max_length=191,blank=True)
	comment=models.CharField(max_length=191,blank=True)
	rating=models.IntegerField(default=1)
	status=models.CharField(max_length=191,choices=status, default='New')
	ip=models.CharField(max_length=191,blank=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.subject

class Color(models.Model):
	name=models.CharField(max_length=191, blank=True)
	code=models.CharField(max_length=191, blank=True)

	def __str__(self):
		return self.name

	def color_tag(self):
		return mark_safe('<span style="background-color:{};color:{}" >Color</span>'.format(self.code,self.code))

class Size(models.Model):
	name=models.CharField(max_length=191, blank=True)
	code=models.CharField(max_length=191, blank=True)

	def __str__(self):
		return self.name

class Varient(models.Model):
	title=models.CharField(max_length=191,blank=True,null=True)
	product=models.ForeignKey(Product, on_delete=models.CASCADE)
	color=models.ForeignKey(Color, on_delete=models.CASCADE)
	size=models.ForeignKey(Size, on_delete=models.CASCADE)
	image_id=models.IntegerField(default=0,blank=True,null=True)
	quantity=models.IntegerField(default=0)
	price=models.FloatField(default=0)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


	def image(self):
		img=Images.objects.get(id=self.image_id)
		if img.id is not None:
			varient_image=img.image.url
		else:
			varient_image=""
		return varient_image
	def image_tag(self):
		img=Images.objects.get(id=self.image_id)
		if img.id is not None:
			return mark_safe('<img src="{}" width="100" height="80" alt="gallery image" />'.format(img.image.url))
		else:
			return ""
		






	
		 	



		



 
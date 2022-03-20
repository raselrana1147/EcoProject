from django.db import models

# Create your models here.

class ContactUs(models.Model):

	STATUS=(
			('New','New'),
			('Read','Read'),
			('Closed','Closed')
		)
	name=models.CharField(max_length=191)
	email=models.EmailField(max_length=191)
	subject=models.CharField(max_length=191)
	message=models.TextField(max_length=500,blank=True)
	status=models.CharField(max_length=191,choices=STATUS,default='New')
	ip=models.CharField(max_length=191,blank=True)
	node=models.CharField(max_length=191,blank=True)
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Faq(models.Model):
	STATUS=(
			('True','True'),
			('False','False')
		)

	order_number=models.CharField(max_length=191,blank=True)
	question=models.CharField(max_length=191)
	answer=models.TextField(max_length=500,blank=True)
	status=models.CharField(max_length=191,choices=STATUS,default='False')
	created_at=models.DateTimeField(auto_now_add=True)
	updated_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question

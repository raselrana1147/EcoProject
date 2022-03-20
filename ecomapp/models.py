from django.db import models

# Create your models here.

class Setting(models.Model):
	STATUS=(
			('True','True'),
			('False','False')
		)
	title=models.CharField(max_length=191)
	kewword=models.CharField(max_length=191)
	address=models.CharField(max_length=191)
	phone=models.CharField(max_length=191)
	fax=models.CharField(max_length=191,blank=True)
	email=models.EmailField(max_length=191,blank=True,null=True)
	smtpserver=models.CharField(max_length=191)
	smtpemail=models.CharField(max_length=191,blank=True,null=True)
	smtppassword=models.CharField(max_length=191,blank=True,null=True)
	smtpport=models.CharField(max_length=191,blank=True)
	icon=models.ImageField(upload_to='icon')
	facebook=models.CharField(max_length=191,blank=True)
	instragram=models.CharField(max_length=191,blank=True)
	contact=models.CharField(max_length=191,blank=True)
	referece=models.TextField(max_length=191,blank=True)
	status=models.CharField(max_length=191,blank=True, choices=STATUS)
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
class Slider(models.Model):

	title=models.CharField(max_length=191,blank=True)
	link=models.CharField(max_length=191, blank=True)
	button_title=models.CharField(max_length=191,blank=True)
	image=models.ImageField(upload_to='slider')
	created_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title





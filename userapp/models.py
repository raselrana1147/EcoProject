from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

# Create your models here.

class UserProfile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.CharField(max_length=191,blank=True)
	address=models.CharField(max_length=191,blank=True)
	city=models.CharField(max_length=191,blank=True)
	country=models.CharField(max_length=191,blank=True)
	image=models.ImageField(upload_to='profile',blank=True)

	def __str__(self):
		return self.user.username

	def full_name(self):
		return self.user.first_name+' '+self.user.last_name

	def profile_image(self):
		return mark_safe('<img src="{}" width="100" height="80" alt="profile image" />'.format(self.image.url))
	

